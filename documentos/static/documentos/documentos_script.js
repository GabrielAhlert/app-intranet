document.addEventListener("DOMContentLoaded", () => {
    const L1 = document.querySelectorAll(".L1 > div");
    const L2 = document.querySelectorAll(".L2 > div");
    const L3 = document.querySelectorAll(".L3 > div");
    const L4 = document.querySelectorAll(".L4 > div");
    const L5 = document.querySelectorAll(".L5 > div");

    // L1.forEach(l1 => {
    //     l1.addEventListener("click", (Event) => {
    //         const child_container = document.getElementById(Event.currentTarget.getAttribute("trigger"));
            
    //         if (!Event.currentTarget.classList.contains("active")){
    //             L1.forEach(l1 => {
    //                 l1.classList.remove("active");
    //             });
    //         }
    //         Event.currentTarget.classList.toggle("active");
            
    //         if (child_container.classList.contains("hidden")) {
    //             L2.forEach(l2 => {
    //                 l2.classList.add("hidden");
    //             });
    //         }
    //         child_container.classList.toggle("hidden");
    //     });
    // });

    function hiddenAll(L){
        L.forEach(l => {
            l.classList.add("hidden");
        });
    }
    function inativeAll(L){
        L.forEach(l => {
            l.classList.remove("active");
        });
    }

    L1.forEach(l1 => {
        l1.addEventListener("click", (Event) => {
            if (!Event.currentTarget.classList.contains("active")){
                inativeAll(L1);
                inativeAll(L2);
                inativeAll(L3);
                inativeAll(L4);
                inativeAll(L5);
            }
            Event.currentTarget.classList.toggle("active");

            hiddenAll(L2);
            hiddenAll(L3);
            hiddenAll(L4);
            hiddenAll(L5);
            L2.forEach(l2 => {
                console.log(l2.getAttribute("parent"));
                console.log(Event.currentTarget.getAttribute("Id"));
                if(l2.getAttribute("parent") == Event.currentTarget.getAttribute("Id"))
                    l2.classList.remove("hidden");
            });

        });
    });

    L2.forEach(l2 => {
        l2.addEventListener("click", (Event) => {
            if (!Event.currentTarget.classList.contains("active")){
                inativeAll(L2);
                inativeAll(L3);
                inativeAll(L4);
                inativeAll(L5);
            }
            Event.currentTarget.classList.toggle("active");

            hiddenAll(L3);
            hiddenAll(L4);
            hiddenAll(L5);
            L3.forEach(l3 => {
                if(l3.getAttribute("parent") == Event.currentTarget.getAttribute("Id"))
                    l3.classList.remove("hidden");
                else
                    l3.classList.add("hidden");
            });
        });
    });

    L3.forEach(l3 => {
        l3.addEventListener("click", (Event) => {
            if (!Event.currentTarget.classList.contains("active")){
                inativeAll(L3);
                inativeAll(L4);
                inativeAll(L5);
            }
            Event.currentTarget.classList.toggle("active");
            hiddenAll(L4);
            hiddenAll(L5);
            L4.forEach(l4 => {
                if(l4.getAttribute("parent") == Event.currentTarget.getAttribute("Id"))
                    l4.classList.remove("hidden");
                else
                    l4.classList.add("hidden");
            });
        });
    });

    L4.forEach(l4 => {
        l4.addEventListener("click", (Event) => {
            if (!Event.currentTarget.classList.contains("active")){
                inativeAll(L4);
                inativeAll(L5);
            }
            Event.currentTarget.classList.toggle("active");
            hiddenAll(L5);
            L5.forEach(l5 => {
                if(l5.getAttribute("parent") == Event.currentTarget.getAttribute("Id"))
                    l5.classList.remove("hidden");
                else
                    l5.classList.add("hidden");
            });
        });
    });
});



