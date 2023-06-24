function pullBancoConvite(){
    const convites = document.getElementById("convites")
    fetch('pullBancoConvites')
    .then(response => response.json())
    .then(data => {
        texto = '<div class="convite" id="header_convites">'
        texto += '<tag>Convite da lista</tag>'
        texto += '<tag>Aceitar?</tag>'
        texto += '<tag>Recusar?</tag>'
        texto += '</div>'
        if (data.convites.length != 0){
            data.convites.forEach(function(convite) {
                // Acessa os valores de cada item
                texto += '<div class="convite">'
                texto += '<tag>' + convite.nome_lista + '</tag>'
                texto += '<tag><a href="responder_convite/"' + convite.id_lista + '/' + convite.usuario + '/1"><img src="static/icons/check_mark.png" width="24px"></a></tag>'
                texto += '<tag><a href="responder_convite/"' + convite.id_lista + '/' + convite.usuario + '/0"><img src="static/icons/checkbox_cross.png" width="24px"></a></tag>'    
                texto += '</div>'        
            })
            convites.innerHTML = texto
        }
        else{
            convites.innerHTML = "Você não recebeu nenhum convite"
        }
    })
    .catch(error => {
        console.error(error);
    });
}