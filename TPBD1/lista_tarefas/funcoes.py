from .models import Usuario, Tarefas, ListaDeTarefas, Convite

def check_usuario_lista(id_usuario, id_lista):
    if ListaDeTarefas.objects.filter(id_lista=id_lista,fk_nome_usuario=id_usuario) or Convite.objects.filter(fk_lista=id_lista,fk_nome_usuario_rec=id_usuario,aceito=1):
        return True
    return False

def listas_usuario(id_usuario):
    return ListaDeTarefas.objects.filter(fk_nome_usuario=id_usuario) | ListaDeTarefas.objects.filter(id_lista__in=Convite.objects.filter(fk_nome_usuario_rec=id_usuario,aceito=1).values_list("fk_lista", flat=True))
