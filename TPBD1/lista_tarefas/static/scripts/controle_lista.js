function criar_Lista(){
    nome = document.getElementById("nome_lista")
    listas = document.getElementById("listas")

    fetch('criar_lista/' + nome.value)
    .then(response => response.json())
    .then(data => {
        if (data.success == true){
            this.alert("Lista criada sucesso!")
            texto = ""
            data.items.forEach(function(item) {
                // Acessa os valores de cada item
                texto = texto + "<a href='lista/"+ item.id +"'>" + item.nome + "</a><br>"
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
    setInterval(pullBanco, 2000); // 15000 milissegundos = 15 segundos
    
})

function pullBanco(){
    const listas = document.getElementById("listas")
    fetch('pullBancoListas')
    .then(response => response.json())
    .then(data => {
        texto = ""
        if (data.listas.length != 0){
            data.listas.forEach(function(lista) {
                // Acessa os valores de cada item
                texto += '<a href="lista/' + lista.id + '">' + lista.texto + '</a><br>'
            })
            listas.innerHTML = texto
        }
        else{
            listas.innerHTML = "Você não está em nenhuma lista"
        }
    })
    .catch(error => {
        console.error(error);
    });
}