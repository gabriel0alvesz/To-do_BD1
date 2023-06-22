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