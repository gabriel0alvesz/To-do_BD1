function cria_tarefa(){
    
}

function attTarefa(id){
    // var check = document.getElementById("checkbox__" + id).checked

    fetch('../../../att_tarefa/' + id + '/1')
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

    fetch('../../../att_tarefa/' + id + '/0')
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