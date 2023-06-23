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
            texto = '<div class="tarefa" id="tarefa__' + data.tarefa.id + '">' + data.tarefa.descricao + '<input type="checkbox" id="checkbox__'
            texto += data.tarefa.id + '" onclick="attTarefa(' +  data.tarefa.id + ')"><input type="button" onclick="deleteTarefa(' + data.tarefa.id + ')">'
            texto += '<br></div>'
            tarefas.innerHTML += texto
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
    setInterval(pullBanco, 2000); // 15000 milissegundos = 15 segundos
    
})

function pullBanco(){
    const tarefas = document.getElementsByClassName("tarefas")[0]
    fetch('../../pullBancoTarefas/' + lista)
    .then(response => response.json())
    .then(data => {
        texto = ""
        data.tarefas.forEach(function(tarefa) {
            // Acessa os valores de cada item
            texto += '<div class="tarefa" id="tarefa__' + tarefa.id + '">' + tarefa.descricao + '<input type="checkbox" id="checkbox__'
            texto += tarefa.id + '" onclick="attTarefa(' +  tarefa.id + ')" '
            if (tarefa.checked){
                texto += "checked"
            }
            texto += '><button onclick="deleteTarefa(' + tarefa.id + ')"><img src="../static/icons/trash_can.png" width="24px"></button>'
            texto += '<br></div>'
        })
        tarefas.innerHTML = texto
    })
    .catch(error => {
        console.error(error);
    });
}