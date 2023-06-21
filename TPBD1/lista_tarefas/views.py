from django.shortcuts import render
from django.db import IntegrityError
from .models import Usuario, Tarefas, ListaDeTarefas, Convite
from django.contrib.auth import authenticate, login, logout # Utilizados para autenticar usuário
from django.http import HttpResponseRedirect 
from django.urls import reverse

from . import funcoes
from datetime import datetime, timezone, timedelta

# Create your views here.

def home(request):
    
    usuarios = len(Usuario.objects.all())
    listas   = len(ListaDeTarefas.objects.all())
    tarefas  = len(Tarefas.objects.all())
    
    if request.user.is_authenticated:
        usuario = request.user
        listas = ListaDeTarefas.objects.filter(fk_nome_usuario=usuario) | ListaDeTarefas.objects.filter(id_lista__in=Convite.objects.filter(fk_nome_usuario_rec=usuario,aceito=1).values_list("fk_lista", flat=True))
        convites = Convite.objects.filter(fk_nome_usuario_rec=usuario,aceito=0)
    else:
        usuario = None
        convites = None
        
    return render(request, "lista_tarefas/home.html", {
        "title": "Home",
        "usuario": usuario,
        "usuarios": usuarios,
        "listas": listas,
        "tarefas": tarefas,
        "convites": convites,
    })

# Views de Administração de Usuario
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "lista_tarefas/login.html", {
                "title": "Login",
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "lista_tarefas/login.html", {
            "title": "Login"
        })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

def registrar(request):
    if request.method == "POST":
        nome_usuario = request.POST["username"]
        email = request.POST["email"]
        nome = request.POST["nome"]
        telefone = request.POST["telefone"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "lista_tarefas/registrar.html", {
                "title": "Registrar",
                "message": "Senhas diferentes."
            })

        # Attempt to create new user
        try:
            user = Usuario.objects.create_user(nome_usuario, password, email, nome, telefone)
            user.save()
        except ValueError as e:
            return render(request, "lista_tarefas/registrar.html", {
                "title": "Registrar",
                "message": e,
            })
        except IntegrityError:
            return render(request, "lista_tarefas/registrar.html", {
                "title": "Registrar",
                "message": "Usuário já utilizado."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "lista_tarefas/registrar.html",{
            "title": "Registrar"
        })
        
# Views de Administrar Listas
def criar_lista(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        # try:
        timezone_offset = -3.0 
        tzinfo = timezone(timedelta(hours=timezone_offset))
        hora_criacao = datetime.now(tzinfo)
        lista = ListaDeTarefas(nome_descritivo=nome,data_hora_criacao=hora_criacao,data_hora_modificacao=hora_criacao,responsavel_modificacao=request.user,fk_nome_usuario=request.user)
        lista.save()
        return render(request, "lista_tarefas/criar_lista.html", {
            "title": "Criar Lista",
            "usuario": request.user,
            "message": "Lista " + nome + " criada com sucesso",
        })
        # except:
        #     return render(request, "lista_tarefas/criar_lista.html", {
        #         "title": "Criar Lista",
        #         "usuario": request.user,
        #         "message": "Falha ao criar a lista",
        #     })            
    return render(request, "lista_tarefas/criar_lista.html", {
        "title": "Criar Lista",
        "usuario": request.user,
    })

def view_lista(request,id,retorno=None):
    lista = ListaDeTarefas.objects.get(id_lista=id)
    tarefas = Tarefas.objects.filter(fk_lista=id)

    try:
        usuario = request.user
    except:
        usuario = None
        
    try:
        booleana = funcoes.check_usuario_lista(request.user.nome_usuario,id)
    except:
        booleana = False
    
    nao_convidado = Usuario.objects.exclude(nome_usuario__in=Convite.objects.filter(fk_lista=id).values_list('fk_nome_usuario_rec', flat=True)).exclude(nome_usuario=lista.fk_nome_usuario).values_list("nome_usuario", flat=True)
    
    # Retorno:
    # 1: Convite enviado com sucesso
    # 2: Tarefa criada com sucesso
    # 3: Tarefa criada, hora de finalização inválida
    # 4: Tarefa não criada

    return render(request, "lista_tarefas/lista.html",{
        "title": lista.nome_descritivo,
        "tarefas": tarefas,
        "lista": lista,
        "perm": booleana,
        "usuario": usuario,
        "nao_convidado": nao_convidado,
        "retorno": retorno,
    })

def criar_convite(request,id_lista,usuario):
    if request.method == 'POST':
        lista = ListaDeTarefas.objects.get(id_lista=id_lista)
        usuario_env = Usuario.objects.get(nome_usuario=usuario)
        usuario_rec = Usuario.objects.get(nome_usuario=request.POST["valor_selecionado"])
        convite = Convite(fk_nome_usuario_env=usuario_env, fk_nome_usuario_rec=usuario_rec, fk_lista=lista,aceito=0)
        convite.save()
        return HttpResponseRedirect(reverse("lista",None,[id_lista,1]))

def criar_tarefa(request,id_lista):
    if request.method == 'POST':
        lista = ListaDeTarefas.objects.get(id_lista=id_lista)
        timezone_offset = -3.0 
        tzinfo = timezone(timedelta(hours=timezone_offset))
        hora_criacao = datetime.now(tzinfo)
        tarefa = Tarefas(descricao=request.POST["texto_tarefa"], data_cadastro=hora_criacao, tarefa_concluida=0, fk_lista=lista)
        tarefa.save()
        if request.POST["date"] != "":
            data_final = datetime.strptime(request.POST["date"], "%Y-%m-%dT%H:%M")
            data_final = data_final.replace(tzinfo=tzinfo)
            tarefa.data_vencimento = request.POST["date"]
            tarefa.save()
        return HttpResponseRedirect(reverse("lista",None,[id_lista,2]))

def responder_convite(request,id_lista,id_usuario,resposta):
    convite = Convite.objects.get(fk_lista=id_lista,fk_nome_usuario_rec=id_usuario)
    if resposta == 0:
        convite.delete()
    else:
        convite.aceito = 1
        convite.save()
    return HttpResponseRedirect(reverse("home"))
