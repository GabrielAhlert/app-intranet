document.querySelector('#cotacao').addEventListener('click', function (Event) {
    random = Math.floor(Math.random() * 1000000);
    href = Event.currentTarget.getAttribute('href').toString();
    if (href.includes('?'))
        href = href.split('?')[0];
    Event.currentTarget.setAttribute('href', href + '?cotacao=' + random);
});

function toggleInputQuickSearch() {
    //Fecha os icones e abre a pesquisa
    if ($('.hide_on_search').css("display") == "none") {
        $('#box_search').hide(10, function () {
            $('.hide_on_search').show();
            $("#icon_search").removeClass('fa-xmark').addClass('fa-magnifying-glass');
            $("#label_search").text("Busca");
            $("#input_search").val('');
            $("#responses_search").hide();
        });
    } else {
        $('.hide_on_search').hide(10, function () {
            $("#icon_search").removeClass('fa-magnifying-glass').addClass('fa-xmark');
            $("#label_search").text("Fechar");
            $("#input_search").val('');
            $("#responses_search").hide();
            $('#box_search').show(0, function () {
                $("#input_search").focus();
            });
        });
    }

    //Abre a pesquisa sem fechar os icones
    // if ($('#box_search').css("display") == "none") {
    //     $("#icon_search").toggleClass('fa-magnifying-glass fa-xmark');
    //     $("#label_search").text("Fechar");
    //     $("#input_search").val('');
    //     $("#input_search").focus();
    //     $("#responses_search").hide();
    //     $('#box_search').show(30, function() {
    //         $("#input_search").focus();
    //     });
    // } else {
    //     $('#box_search').hide();
    //     $("#icon_search").toggleClass('fa-xmark fa-magnifying-glass');
    //     $("#label_search").text("Busca");
    //     $("#input_search").val('');
    //     $("#responses_search").hide();
    // }
}

$("#toggle_search").on("click", function () {
    toggleInputQuickSearch();
});

$(document).on("click", function (event) {
    var $target = $(event.target);

    if (!$target.closest('#toggle_search').length) {
        $("#responses_search").hide();
    }
});

$("#responses_search").on("click", function (event) {
    event.stopPropagation();
});

$("#modalRamais").on("shown.bs.modal", function() {
    $("#search_ramal").focus();
})

$("#input_search").on("input", function () {
    var inputLength = $("#input_search").val().length;
    if (inputLength > 2) {
        $("#responses_search").show();

        $.ajax({
            method: "GET",
            url: "/search/get_quicksearch/" + $("#input_search").val(),
            success: function (response) {
                $("#list_results_quicksearch").empty();
                for (const key in response) {
                    if (key === 'contatos' && response[key].length > 0) {
                        const contatos = response[key];
                        const cabecalho = $("<span>").text("Contatos").addClass("fw-bold");
                        const contatos_li = $("<li>").addClass("list-group-item").append(cabecalho);
                        const contatos_ul = $("<ul>").addClass("list-group list-group-flush");

                        contatos.forEach(item => {
                            const list = $("<li>").addClass("list-group-item");
                            const nome = $("<span>").addClass("fw-semibold").text(item.nome);

                            let funcao = "";
                            if (item.funcao) {
                                funcao = $("<span>").addClass("fw-lighter").text(item.funcao);
                            }

                            let ramal = "";
                            if (item.ramal) {
                                ramal = $("<span>").text(" - Ramal " + item.ramal);
                            }

                            let email = "";
                            if (item.email || item.email != '-') {
                                email = $("<span>").text(item.email);
                            }

                            const br = $("<br>");

                            const titulo = $("<span>").append(nome).append(ramal);

                            list.append(titulo, br.clone(), funcao, br.clone(), email);

                            contatos_ul.append(list);
                        });

                        $(contatos_li).append(contatos_ul);
                        $("#list_results_quicksearch").append(contatos_li);

                    } else if (key === 'documentos' && response[key].length > 0) {                        
                        const documentos = response[key];

                        const cabecalho = $("<span>").text("Documentos").addClass("fw-bold");
                        const documentos_li = $("<li>").addClass("list-group-item").append(cabecalho);
                        const documentos_ul = $("<ul>").addClass("list-group list-group-flush");

                        documentos.forEach(item => {
                            console.log(item);
                            const list = $("<li>").addClass("list-group-item");
                            const nome = $("<span>").addClass("fw-semibold").text(item.nome);
                            const dados = $("<span>").text(item.categoria).addClass("fw-lighter");
                            const br = $("<br>");

                            const titulo = $("<span>").append($("<a>").append(nome).attr("href", '/documentos/download/' + item.id).attr("target", '_blank')).append(" - ").append(dados);
                            list.append(titulo);

                            documentos_ul.append(list);
                        });

                        $(documentos_li).append(documentos_ul);
                        $("#list_results_quicksearch").append(documentos_li);
                    }
                }
            },
            error: function (error) {
                console.error(error);
            }
        });
    } else {
        $("#responses_search").hide();
    }
});

const scrollContainer = document.querySelector('.drag-scroll');

let isDragging = false;
let startX;
let scrollLeft;
let clickTimer;

scrollContainer.addEventListener('mousedown', (e) => {
    e.preventDefault(); 
    clickTimer = setTimeout(() => {
        isDragging = true;
        scrollContainer.classList.add('dragging');
        startX = e.pageX - scrollContainer.offsetLeft;
        scrollLeft = scrollContainer.scrollLeft;
    }, 150); 
});

scrollContainer.addEventListener('mouseup', (e) => {
    clearTimeout(clickTimer); 
    if (isDragging) {
        e.preventDefault(); 
        e.stopPropagation();
    }
    isDragging = false;
    scrollContainer.classList.remove('dragging');
});

scrollContainer.addEventListener('mouseleave', () => {
    clearTimeout(clickTimer);
    isDragging = false;
    scrollContainer.classList.remove('dragging');
});

scrollContainer.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    e.preventDefault();
    const x = e.pageX - scrollContainer.offsetLeft;
    const walk = (x - startX) * 2;
    scrollContainer.scrollLeft = scrollLeft - walk;
});

scrollContainer.addEventListener('click', (e) => {
    if (isDragging) {
        e.preventDefault();
        e.stopPropagation();
    }
});