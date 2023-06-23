function pullBancoConvite(){
    const convites = document.getElementById("convites")
    fetch('pullBancoConvites')
    .then(response => response.json())
    .then(data => {
        texto = ""
        if (data.convites.length != 0){
            data.convites.forEach(function(convite) {
                // Acessa os valores de cada item
                texto += 'Convite da lista: ' + convite.nome_descritivo + '<br>'
                texto += '<a href="responder_convite/"' + convite.id_lista + '/' + convite.usuario + '/0">Recusar' + convite.nome_descritivo + '</a><br>'
                texto += '<a href="responder_convite/"' + convite.id_lista + '/' + convite.usuario + '/1">Recusar' + convite.nome_descritivo + '</a><br>'            
            })
            convites.innerHTML = texto
        }
        else{
            convites.innerHTML = "Você não tem nenhum convite"
        }
    })
    .catch(error => {
        console.error(error);
    });
}