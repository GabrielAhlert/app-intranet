document.addEventListener("DOMContentLoaded", () => {
    const L1 = document.querySelectorAll(".L1 > div");
    const L2 = document.querySelectorAll(".L2 > div");
    const L3 = document.querySelectorAll(".L3 > div");
    const L4 = document.querySelectorAll(".L4 > div");
    const L5 = document.querySelectorAll(".L5 > div");
    const header = document.querySelector(".header");
    const footer = document.querySelector(".footer");
    const back = document.querySelectorAll(".back");


    header.classList.add("sticky-top");
    footer.classList.add("sticky-bottom");

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

    back.forEach(b => {
        b.addEventListener("click", (Event) => {
           const target_str =  Event.currentTarget.getAttribute("target");
           const target = document.querySelector("."+target_str);


           if (target_str == "L1"){
               hiddenAll([L2,L3,L4,L5]);
               inativeAll([L1,L2,L3,L4,L5]);
               document.querySelector("body").scrollIntoView({behavior: "smooth"});
           }
            if (target_str == "L2"){
                hiddenAll([L3,L4,L5]);
                inativeAll([L2,L3,L4,L5]);
                target.scrollIntoView({behavior: "smooth"});
            }
            if (target_str == "L3"){
                hiddenAll([L4,L5]);
                inativeAll([L3,L4,L5]);
                target.scrollIntoView({behavior: "smooth"});
            } 
            if (target_str == "L4"){
                hiddenAll([L5]);
                inativeAll([L4,L5]);
                target.scrollIntoView({behavior: "smooth"});
            }
        });
    });
        

    L1.forEach(l1 => {
        if(!l1.classList.contains("back") && !l1.classList.contains("doc"))
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
        if(!l2.classList.contains("back") && !l2.classList.contains("doc"))
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
                    document.querySelector(".L3").scrollIntoView({behavior: "smooth", inline: "nearest"});
                }
                Event.currentTarget.classList.toggle("active");
            });
    });

    L3.forEach(l3 => {
        if(!l3.classList.contains("back") && !l3.classList.contains("doc"))
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
                    document.querySelector(".L4").scrollIntoView({behavior: "smooth", inline: "nearest"});
                }
                Event.currentTarget.classList.toggle("active");
            });
    });

    L4.forEach(l4 => {
        if(!l4.classList.contains("back") && !l4.classList.contains("doc"))
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
                    document.querySelector(".L5").scrollIntoView({behavior: "smooth", inline: "nearest"});
                }
                Event.currentTarget.classList.toggle("active");
            });
    });
});



