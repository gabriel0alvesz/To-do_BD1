function cria_tarefa(id_lista){
    const tarefa = document.getElementById("texto_tarefa")
    const dia = document.getElementById("date")
    const tarefas = document.getElementsByClassName("tarefas")[0]

    if (dia.value != ""){
        data = dia.value
    }
    else{
        data = "-1"
    }

    fetch('../../../criar_tarefa/' + id_lista + '/' + tarefa.value + '/' + data)
    .then(response => response.json())
    .then(data => {
        if (data.success){
            alert("Tarefa criada com sucesso")
            console.log(data)
            texto = '<div class="tarefa" id="tarefa__' + data.tarefa.id + '">'
            texto += '<tag>' + data.tarefa.descricao + '</tag>'

            cadastro = new Date(data.tarefa.data_cadastro)
            a1 = cadastro.getFullYear()
            m1 = cadastro.getMonth() + 1
            d1 = cadastro.getDate()
            h1 = cadastro.getHours()
            min1 = cadastro.getMinutes() 

            if (m1 < 10) m1 = '0' + m1
            if (d1 < 10) d1 = '0' + d1
            if (h1 < 10) h1 = '0' + h1
            if (min1 < 10) min1 = '0' + min1
            texto += '<tag>' + d1 + '/' + m1 + '/' + a1 + ' ' + h1 + ':' + min1 + '</tag>'

            texto += '<tag>'
            if(data.tarefa.data_vencimento) {
                vencimento = new Date(data.tarefa.data_vencimento)
                a2 = vencimento.getFullYear()
                m2 = vencimento.getMonth() + 1
                d2 = vencimento.getDate()
                h2 = vencimento.getHours()
                min2 = vencimento.getMinutes() 

                if (m2 < 10) m2 = '0' + m2
                if (d2 < 10) d2 = '0' + d2
                if (h2 < 10) h2 = '0' + h2
                if (min2 < 10) min2 = '0' + min2
                texto += d2 + '/' + m2 + '/' + a2 + ' ' + h2 + ':' + min2
            }
            texto += '</tag>'
            texto += '<div><input type="checkbox" class="checkbox_tarefa" id="checkbox__' + data.tarefa.id + '" onclick="attTarefa(' +  data.tarefa.id + ')"></div>' 
            texto += '<input type="button" onclick="deleteTarefa(' + data.tarefa.id + ')">'
            texto += '<br></div>'
            tarefas.innerHTML += texto

            tarefa.value = ""
            dia.value = ""
        }
    })
    .catch(error => {
        console.error(error);
    });}

function attTarefa(id){
    // var check = document.getElementById("checkbox__" + id).checked

    fetch('../../att_tarefa/' + id + '/1')
    .then(response => response.json())
    .then(data => {
        if (data.success){
            alert("Tarefa atualizada com sucesso")
        }
    })
    .catch(error => {
        console.error(error);
    });
}

function deleteTarefa(id){
    // var check = document.getElementById("checkbox__" + id).checked

    fetch('../../att_tarefa/' + id + '/0')
    .then(response => response.json())
    .then(data => {
        if (!data.success){
            var tarefa = document.getElementById("tarefa__" + id)
            tarefa.remove()
            alert("Tarefa deletada com sucesso")
        }
    })
    .catch(error => {
        console.error(error);
    });
}

window.addEventListener('load', function() {
    setInterval(pullBanco, 5000); // 15000 milissegundos = 15 segundos
    
})

function pullBanco(){
    const tarefas = document.getElementsByClassName("tarefas")[0]
    fetch('../../pullBancoTarefas/' + lista)
    .then(response => response.json())
    .then(data => {
        if (data.success == "True"){
            texto = '<div class="tarefa" id="header_tarefas">'
            texto += '<tag>Descrição da tarefa</tag>'
            texto += '<tag>Data de Criação</tag>'
            texto += '<tag>Data de Vencimento</tag>'
            texto += '<tag>Concluída?</tag>'
            texto += '<tag>Deletar?</tag>'
            texto += '</div>'
            if (data.tarefas.length != 0){
                data.tarefas.forEach(function(tarefa) {
                    // Acessa os valores de cada item
                    texto += '<div class="tarefa" id="tarefa__' + tarefa.id + '">'
                    texto += '<tag>' + tarefa.descricao + '</tag>'

                    cadastro = new Date(tarefa.data_cadastro)
                    a1 = cadastro.getFullYear()
                    m1 = cadastro.getMonth() + 1
                    d1 = cadastro.getDate()
                    h1 = cadastro.getHours()
                    min1 = cadastro.getMinutes() 

                    if (m1 < 10) m1 = '0' + m1
                    if (d1 < 10) d1 = '0' + d1
                    if (h1 < 10) h1 = '0' + h1
                    if (min1 < 10) min1 = '0' + min1
                    texto += '<tag>' + d1 + '/' + m1 + '/' + a1 + ' ' + h1 + ':' + min1 + '</tag>'

                    texto += '<tag>' 
                    if(tarefa.data_vencimento) {
                        vencimento = new Date(tarefa.data_vencimento)
                        a2 = vencimento.getFullYear()
                        m2 = vencimento.getMonth() + 1
                        d2 = vencimento.getDate()
                        h2 = vencimento.getHours()
                        min2 = vencimento.getMinutes() 

                        if (m2 < 10) m2 = '0' + m2
                        if (d2 < 10) d2 = '0' + d2
                        if (h2 < 10) h2 = '0' + h2
                        if (min2 < 10) min2 = '0' + min2
                        texto += d2 + '/' + m2 + '/' + a2 + ' ' + h2 + ':' + min2
                    }
                    texto += '</tag>'
                    texto += '<div><input type="checkbox" class="checkbox_tarefa" id="checkbox__' + tarefa.id + '" onclick="attTarefa(' +  tarefa.id + ')" '
                    if (tarefa.checked){
                        texto += "checked"
                    }
                    texto += '></div>' 
                    texto += '<button onclick="deleteTarefa(' + tarefa.id + ')"><img src="../static/icons/trash_can.png" width="24px"></button>'
                    texto += '<br></div>'
                })
                tarefas.innerHTML = texto
            }
            else{
                tarefas.innerHTML = "Não existe nenhuma tarefa nesta Lista"
            }
        }
        else{
            alert("A lista foi excluida por seu criador")
            window.location.href = "/";
        }
    })
    .catch(error => {
        console.error(error);
    });
}

function limpar_campos() {
    const tarefa = document.getElementById("texto_tarefa")
    const dia = document.getElementById("date")
    tarefa.value = ""
    dia.value = ""
}