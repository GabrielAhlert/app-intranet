document.addEventListener("DOMContentLoaded", () => {
    const L1 = document.querySelectorAll(".L1 > div");
    const L2 = document.querySelectorAll(".L2");

    L1.forEach(l1 => {
        l1.addEventListener("click", (Event) => {
            const child_container = document.getElementById(Event.currentTarget.getAttribute("trigger"));
            
            if (!Event.currentTarget.classList.contains("active")){
                L1.forEach(l1 => {
                    l1.classList.remove("active");
                });
            }
            Event.currentTarget.classList.toggle("active");
            
            if (child_container.classList.contains("hidden")) {
                L2.forEach(l2 => {
                    l2.classList.add("hidden");
                });
            }
            child_container.classList.toggle("hidden");
        });
    });
});



