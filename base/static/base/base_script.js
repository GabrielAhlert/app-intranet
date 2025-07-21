document.querySelector('#cotacao').addEventListener('click', function (Event) {
    random = Math.floor(Math.random() * 1000000);
    href = Event.currentTarget.getAttribute('href').toString();
    if (href.includes('?'))
        href = href.split('?')[0];
    Event.currentTarget.setAttribute('href', href + '?cotacao=' + random);
});

$("#modalRamais").on("shown.bs.modal", function () {
    $("#search_ramal").focus();
})

$("#input_search").on("input", function () {
    var inputLength = $("#input_search").val().length;
    if (inputLength > 2) {
        $.ajax({
            method: "GET",
            url: "/search/get_quicksearch/" + $("#input_search").val(),
            success: function (response) {
                $("#list_results_quicksearch").empty();
                for (const key in response) {
                    if (key === 'contatos' && response[key].length > 0) {
                        const contatos = response[key];

                        const groupedByUnidade = {};

                        contatos.forEach(item => {
                            const unidade = item.unidade || "Sem unidade";

                            if (!groupedByUnidade[unidade]) {
                                groupedByUnidade[unidade] = [];
                            }

                            groupedByUnidade[unidade].push(item);
                        });

                        const cabecalho = $("<h5>").text("Contatos").addClass("result-quicksearch-type");
                        const contatos_li = $("<li>").addClass("list-group-item").append(cabecalho);
                        const contatos_ul = $("<ul>").addClass("list-group list-group-flush result-quicksearch-filial-list");

                        Object.keys(groupedByUnidade).forEach(unidade => {
                            const unidadeHeader = $("<li>").addClass("list-group-item fw-bold").append($("<span>").addClass("title-filial").text(unidade));
                            const unidadeList = $("<ul>").addClass("list-group list-group-flush result-quicksearch-contact-list");

                            groupedByUnidade[unidade].forEach(item => {
                                const list = $("<li>").addClass("list-group-item");
                                const nome = $("<span>").addClass("fw-semibold").text(item.nome);

                                let funcao = "";
                                if (item.funcao) {
                                    funcao = $("<span>").addClass("fw-lighter").text(item.funcao);
                                }

                                let telefone = "";
                                if (item.telefone) {
                                    telefone = " - " + item.telefone;
                                }

                                let ramal = "";
                                let email = "";
                                if (item.ramal) {
                                    ramal = " - Ramal " + item.ramal;
                                }
                                if (item.email && item.email !== '-') {
                                    email = $("<span>").text(item.email + ramal + telefone);
                                }

                                const br = $("<br>")
                                const titulo = $("<span>").append(nome);

                                list.append(
                                    titulo,
                                    document.createTextNode(" - "),
                                    funcao,
                                    br.clone(),
                                    email
                                );
                                unidadeList.append(list);
                            });

                            contatos_ul.append(unidadeHeader);
                            contatos_ul.append(unidadeList);
                        });

                        $(contatos_li).append(contatos_ul);
                        $("#list_results_quicksearch").append(contatos_li);
                    } else if (key === 'documentos' && response[key].length > 0) {
                        const documentos = response[key];

                        const cabecalho = $("<h5>").text("Documentos").addClass("result-quicksearch-type");
                        const documentos_li = $("<li>").addClass("list-group-item").append(cabecalho);
                        const documentos_ul = $("<ul>").addClass("list-group list-group-flush");

                        documentos.forEach(item => {
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
        $("#list_results_quicksearch").empty();
    }
});

$("#modalSearch").on('shown.bs.modal', function () {
    $("#input_search").focus();
});

$("#modalSearch").on('hide.bs.modal', function () {
    $("#input_search").val('');
    $("#list_results_quicksearch").empty();
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