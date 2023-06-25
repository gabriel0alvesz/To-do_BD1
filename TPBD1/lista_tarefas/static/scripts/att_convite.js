function pullBancoConvite(){
    console.log("Ok")
    const convites = document.getElementById("convites")
    fetch('pullBancoConvites')
    .then(response => response.json())
    .then(data => {
        texto = '<div class="convite" id="header_convites">'
        texto += '<tag>Convite da lista</tag>'
        texto += '<tag>Dono da lista</tag>'
        texto += '<tag id="tag_aceitar_recusar">Aceitar/Recusar</tag>'
        texto += '</div>'
        if (data.convites.length != 0){
            data.convites.forEach(function(convite) {
                // Acessa os valores de cada item
                texto += '<div class="convite">'
                texto += '<tag>' + convite.nome_lista + '</tag>'
                texto += '<tag>' + convite.dono_lista + '</tag>'
                texto += '<div class="aceitar_recusar">'
                texto += '<a href="responder_convite/' + convite.id_lista + '/' + convite.usuario + '/1"><img src="static/icons/check_mark.png" width="24px"></a>'
                texto += '<div class="vl"></div>'
                texto += '<a href="responder_convite/' + convite.id_lista + '/' + convite.usuario + '/0"><img src="static/icons/checkbox_cross.png" width="24px"></a>'
                texto += '</div>'
                texto += '</div>'        
            })
            if (convites.innerHTML != texto) convites.innerHTML = texto
        }
        else{
            convites.innerHTML = "Você não recebeu nenhum convite"
        }
    })
    .catch(error => {
        console.error(error);
    });
}

function show_convites() {
    const content = document.getElementById("dropdown_convites_content")
    if(content.style.display == "none") {
        pullBancoConvite()
        content.style.display = "block"
    }
    else
        content.style.display = "none"
}