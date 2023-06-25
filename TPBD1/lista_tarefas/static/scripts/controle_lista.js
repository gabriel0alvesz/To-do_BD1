function criar_Lista(){
    nome = document.getElementById("nome_lista")
    listas = document.getElementById("listas")

    fetch('criar_lista/' + nome.value)
    .then(response => response.json())
    .then(data => {
        if (data.success == true){
            this.alert("Lista criada sucesso!")
            texto = '<div class="lista" id="header_listas">'
            texto += '<tag>Nome da lista</tag>'
            texto += '<tag>Data de criação</tag>'
            texto += '<tag>Data da última modificação</tag>'
            texto += '<tag>Responsável pela modificação</tag></div>'
            data.items.forEach(function(item) {
                // Acessa os valores de cada item'
                texto += '<a class="lista" href="lista/' + item.id + '">'
                texto += '<tag>' + item.nome_descritivo + '</tag>'

                criacao = new Date(item.criacao)
                a1 = criacao.getFullYear()
                m1 = criacao.getMonth() + 1
                d1 = criacao.getDate()
                h1 = criacao.getHours()
                min1 = criacao.getMinutes() 

                if (m1 < 10) m1 = '0' + m1
                if (d1 < 10) d1 = '0' + d1
                if (h1 < 10) h1 = '0' + h1
                if (min1 < 10) min1 = '0' + min1
                texto += '<tag>' + d1 + '/' + m1 + '/' + a1 + ' ' + h1 + ':' + min1 + '</tag>'

                modificacao = new Date(item.modificacao)
                a2 = modificacao.getFullYear()
                m2 = modificacao.getMonth() + 1
                d2 = modificacao.getDate()
                h2 = modificacao.getHours()
                min2 = modificacao.getMinutes() 

                if (m2 < 10) m2 = '0' + m2
                if (d2 < 10) d2 = '0' + d2
                if (h2 < 10) h2 = '0' + h2
                if (min2 < 10) min2 = '0' + min2
                texto += '<tag>' + d2 + '/' + m2 + '/' + a2 + ' ' + h2 + ':' + min2 + '</tag>'
                texto += '<tag>' + item.responsavel + '</tag></a>'
            })
            listas.innerHTML = texto
        }
        else{
            this.alert("Lista não criada!")
        }
        nome.value = ""
    })
    .catch(error => {
        console.error(error)
    })
}

window.addEventListener('load', function() {
    const listas = document.getElementById("listas")
    if(listas != null)
        setInterval(pullBanco, 5000); // 15000 milissegundos = 15 segundos
    
})

function pullBanco(){
    const listas = document.getElementById("listas")
    fetch('pullBancoListas')
    .then(response => response.json())
    .then(data => {
        if(data.success == "True") {
            texto = '<div class="lista" id="header_listas">'
            texto += '<tag>Nome da lista</tag>'
            texto += '<tag>Data de criação</tag>'
            texto += '<tag>Data da última modificação</tag>'
            texto += '<tag>Responsável pela modificação</tag>'
            texto += '</div>'
            if (data.listas.length != 0){
                data.listas.forEach(function(lista) {
                    // Acessa os valores de cada item
                    texto += '<a class="lista" href="lista/' + lista.id + '">'
                    texto += '<tag>' + lista.texto + '</tag>'
                    
                    criacao = new Date(lista.criacao)
                    a1 = criacao.getFullYear()
                    m1 = criacao.getMonth() + 1
                    d1 = criacao.getDate()
                    h1 = criacao.getHours()
                    min1 = criacao.getMinutes() 

                    if (m1 < 10) m1 = '0' + m1
                    if (d1 < 10) d1 = '0' + d1
                    if (h1 < 10) h1 = '0' + h1
                    if (min1 < 10) min1 = '0' + min1
                    texto += '<tag>' + d1 + '/' + m1 + '/' + a1 + ' ' + h1 + ':' + min1 + '</tag>'

                    modificacao = new Date(lista.modificacao)
                    a2 = modificacao.getFullYear()
                    m2 = modificacao.getMonth() + 1
                    d2 = modificacao.getDate()
                    h2 = modificacao.getHours()
                    min2 = modificacao.getMinutes() 

                    if (m2 < 10) m2 = '0' + m2
                    if (d2 < 10) d2 = '0' + d2
                    if (h2 < 10) h2 = '0' + h2
                    if (min2 < 10) min2 = '0' + min2
                    texto += '<tag>' + d2 + '/' + m2 + '/' + a2 + ' ' + h2 + ':' + min2 + '</tag>'
                    
                    texto += '<tag>' + lista.responsavel + '</tag>'
                    texto += '</a>'
                })
                listas.innerHTML = texto
            }
        }
        else{
            listas.innerHTML = "Você não está em nenhuma lista"
        }
    })
    .catch(error => {
        console.error(error);
    });
}