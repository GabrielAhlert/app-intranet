const daysTag = document.querySelector(".days"), 
    currentDate = document.querySelector(".current-date"),
    prevNextIcon = document.querySelectorAll(".icons span");

let date = new Date(),
currYear = date.getFullYear(),
currMonth = date.getMonth();

const months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

async function put_event_popover(days){
    const events = await fetch(`/get_eventos_mes/${currMonth+1}-${currYear}/`);
    const eventsJson = await events.json();
    days.forEach(day => {
        const date = new Date(currYear, currMonth, day);
        const events_day = eventsJson.filter(event => event.data == day);
        const li = document.querySelector(`.days li[id="${day}"]`);
        li.setAttribute("data-bs-toggle", "popover");
        li.setAttribute("title", `Eventos do dia ${date.toLocaleDateString()}`);
        let content = "";
        events_day.forEach(event => {
            content += `<p>${event.titulo} - ${event.local}</p>`;
            });
        li.setAttribute("data-bs-content", content);
        li.setAttribute("data-bs-html", "true");
        li.setAttribute("data-bs-placement", "top");
        li.setAttribute("data-bs-trigger", "hover");
    });

    const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
    const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
}

async function put_event_badge(){
    const events = await fetch(`/get_days_with_events/${currMonth+1}-${currYear}/`);
    const eventsJson = await events.json();
    eventsJson.forEach(day => {
        const li = document.querySelector(`.days li[id="${day}"]`);
        li.classList.add("day-with-event");
    });
    //put_event_popover(eventsJson);
}




const renderCalendar = () => {
    let firstDayofMonth = new Date(currYear, currMonth, 1).getDay(),
    lastDateofMonth = new Date(currYear, currMonth + 1, 0).getDate(),
    lastDayofMonth = new Date(currYear, currMonth, lastDateofMonth).getDay(),
    lastDateofLastMonth = new Date(currYear, currMonth, 0).getDate();
    let liTag = "";

    for (let i = firstDayofMonth; i > 0; i--) {
        liTag += `<li class="inactive">${lastDateofLastMonth - i + 1}</li>`;
    }

    for (let i = 1; i <= lastDateofMonth; i++) {
        let isToday = i === date.getDate() && currMonth === new Date().getMonth() && currYear === new Date().getFullYear() ? "today" : ""; 
        liTag += `<li class="${isToday}" id="${i}">${i}</li>`;
    }

    for (let i = lastDayofMonth; i < 6; i++) {
        liTag += `<li class="inactive">${i - lastDayofMonth + 1}</li>`
    }
    currentDate.innerText = `${months[currMonth]} ${currYear}`;
    daysTag.innerHTML = liTag;

    let days = document.querySelectorAll(".days li");

    days.forEach(day => {
        day.addEventListener("click", () => {
            if (day.classList.contains("inactive")) return;
            try {
                document.querySelector(".SelectedDay").classList.remove("SelectedDay");
            } catch (error) {
                console.log("No SelectedDay class");
            }
            day.classList.add("SelectedDay");
            loadEvents(new Date(currYear, currMonth, day.id));
        });
    });
    
    put_event_badge();
}
renderCalendar();

prevNextIcon.forEach(icon => {
    icon.addEventListener("click", () => {
        if (icon.id === "today") {
            currYear = date.getFullYear();
            currMonth = date.getMonth();
        } else
            currMonth = icon.id === "prev" ? currMonth - 1 : currMonth + 1;

        if (currMonth < 0 || currMonth > 11) {
            date = new Date(currYear, currMonth);
            currYear = date.getFullYear();
            currMonth = date.getMonth();
        } else {
            date = new Date();
        }
        renderCalendar();
    });
});

async function loadEvents(date){
    const h1 = document.getElementById("h1-eventos");
    const ul = document.getElementById("ul-eventos");
    h1.innerHTML = "Eventos do dia " + date.toLocaleDateString();
    const events = await fetch(`/get_eventos/${date.toLocaleDateString().replace(/\//g, "-")}/`);
    const eventsJson = await events.json();
    ul.innerHTML = "";
    eventsJson.forEach(event => {
        const li = document.createElement("li");
        li.innerHTML = event.titulo + " - " + event.local;
        ul.appendChild(li);
    });

}

loadEvents(date);




