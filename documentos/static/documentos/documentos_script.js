document.addEventListener("DOMContentLoaded", () => {
    const L1 = document.querySelectorAll(".L1 > div");
    const L2 = document.querySelectorAll(".L2 > div");
    const L3 = document.querySelectorAll(".L3 > div");
    const L4 = document.querySelectorAll(".L4 > div");
    const L5 = document.querySelectorAll(".L5 > div");
    const back = document.querySelectorAll(".back");



    function hiddenAll(Listas){
        Listas.forEach(lista => {
            lista.forEach(l => {
                l.classList.add("hidden");
            });
        });
    }
    function inativeAll(Listas){
        Listas.forEach(lista => {
            lista.forEach(l => {
                l.classList.remove("active");
            });
        });
    }

    // back.forEach(b => {
    //     b.addEventListener("click", (Event) => {
    //         target = document.querySelector(`.${Event.currentTarget.getAttribute("target")}`);
    //         console.log(target);
    //         if (Event.currentTarget.getAttribute("target") == "L1"){
    //             hiddenAll([L3,L4,L5]);
    //             inativeAll([L2,L3,L4,L5]);
    //         }
    //         if (Event.currentTarget.getAttribute("target") == "L2"){
    //             hiddenAll([L4,L5]);
    //             inativeAll([L3,L4,L5]);
    //         }
    //         if (Event.currentTarget.getAttribute("target") == "L3"){
    //             hiddenAll([L5]);
    //             inativeAll([L4,L5]);
    //         }
    //         if (Event.currentTarget.getAttribute("target") == "L4"){
    //             inativeAll([L5]);
    //         }
    //         target.scrollIntoView({behavior: "smooth", inline: "nearest"});
    //     });
    // });




    L1.forEach(l1 => {
        l1.addEventListener("click", (Event) => {
            hiddenAll([L2,L3,L4,L5]);
            if (!Event.currentTarget.classList.contains("active")){
                inativeAll([L1,L2,L3,L4,L5]);
                L2.forEach(l2 => {
                    if(l2.getAttribute("parent") == Event.currentTarget.getAttribute("Id") || l2.classList.contains("back"))
                        l2.classList.remove("hidden");
                });
                
                document.querySelector(".L2").scrollIntoView({behavior: "smooth", inline: "nearest"});
            }
            Event.currentTarget.classList.toggle("active");

        });
    });

    L2.forEach(l2 => {
        l2.addEventListener("click", (Event) => {
            hiddenAll([L3,L4,L5]);
            if (!Event.currentTarget.classList.contains("active")){
                inativeAll([L2,L3,L4,L5])
                L3.forEach(l3 => {
                    if(l3.getAttribute("parent") == Event.currentTarget.getAttribute("Id") || l3.classList.contains("back"))
                        l3.classList.remove("hidden");
                    else
                        l3.classList.add("hidden");
                });
                //L3[0].scrollIntoView({behavior: "smooth", inline: "nearest"});
            }
            Event.currentTarget.classList.toggle("active");
        });
    });

    L3.forEach(l3 => {
        l3.addEventListener("click", (Event) => {
            hiddenAll([L4,L5]);
            if (!Event.currentTarget.classList.contains("active")){
                inativeAll([L3,L4,L5]);
                L4.forEach(l4 => {
                    if(l4.getAttribute("parent") == Event.currentTarget.getAttribute("Id") || l4.classList.contains("back"))
                        l4.classList.remove("hidden");
                    else
                        l4.classList.add("hidden");
                });
                //L4[0].scrollIntoView({behavior: "smooth", inline: "nearest"});
            }
            Event.currentTarget.classList.toggle("active");
        });
    });

    L4.forEach(l4 => {
        l4.addEventListener("click", (Event) => {
            hiddenAll([L5]);
            if (!Event.currentTarget.classList.contains("active")){
                inativeAll([L4,L5]);
                L5.forEach(l5 => {
                    if(l5.getAttribute("parent") == Event.currentTarget.getAttribute("Id") || l5.classList.contains("back"))
                        l5.classList.remove("hidden");
                    else
                        l5.classList.add("hidden");
                });
            }
            Event.currentTarget.classList.toggle("active");
        });
    });
});



