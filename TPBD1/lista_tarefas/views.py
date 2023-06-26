from django.shortcuts import render
from django.db import IntegrityError
from .models import Usuario, Tarefas, ListaDeTarefas, Convite
from django.contrib.auth import authenticate, login, logout # Utilizados para autenticar usuário
from django.http import HttpResponseRedirect 
from django.urls import reverse

from . import funcoes
from datetime import datetime, timezone, timedelta
from django.http import JsonResponse

from re import findall

# Create your views here.

def home(request):
    
    usuarios = len(Usuario.objects.all())
    listas   = len(ListaDeTarefas.objects.all())
    tarefas  = len(Tarefas.objects.all())
    
    if request.user.is_authenticated:
        usuario = request.user
        listas = funcoes.listas_usuario(usuario.nome_usuario)
        convites = Convite.objects.filter(fk_nome_usuario_rec=usuario,aceito=0)
        return render(request, "lista_tarefas/home.html", {
            "title": "Home",
            "usuario": usuario,
            "usuarios": usuarios,
            "listas": listas,
            "tarefas": tarefas,
            "convites": convites,
        })
    else:
        usuario = None
        convites = None
        return render(request, "lista_tarefas/login.html", {
            "title": "Login"
        })
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
        telefone = findall(r'\d+', telefone)
        telefone = ''.join(telefone)

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
                "message": "Nome de usuário já utilizado."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "lista_tarefas/registrar.html",{
            "title": "Registrar"
        })
        
# Views de Listas
def criar_lista(request, nome):
    try:
        nome = nome
        timezone_offset = -3.0 
        tzinfo = timezone(timedelta(hours=timezone_offset))
        hora_criacao = datetime.now(tzinfo)
        lista = ListaDeTarefas(nome_descritivo=nome,data_hora_criacao=hora_criacao,data_hora_modificacao=hora_criacao,responsavel_modificacao=request.user,fk_nome_usuario=request.user)
        lista.save()

        listas = funcoes.listas_usuario(request.user.nome_usuario)

        data = {
            'success': True,
            'items': []
        }

        for item in listas:
            aux = {}
            aux["id"] = item.id_lista
            aux["nome"] = item.nome_descritivo
            aux["criacao"] = item.data_hora_criacao
            aux["modificacao"] = item.data_hora_modificacao
            aux["responsavel"] = item.responsavel_modificacao
            data["items"].append(aux)
        
        return JsonResponse(data)
    except:
        JsonResponse({'success': False})

def view_lista(request,id):
    try:
        lista = ListaDeTarefas.objects.get(id_lista=id)
        tarefas = Tarefas.objects.filter(fk_lista=id)

        try:
            usuario = request.user
            convites = Convite.objects.filter(fk_nome_usuario_rec=usuario,aceito=0)
        except:
            usuario = None
            
        try:
            booleana = funcoes.check_usuario_lista(request.user.nome_usuario,id)
        except:
            booleana = False
        
        nao_convidado = Usuario.objects.exclude(nome_usuario__in=Convite.objects.filter(fk_lista=id).values_list('fk_nome_usuario_rec', flat=True)).exclude(nome_usuario=lista.fk_nome_usuario).values_list("nome_usuario", flat=True)
        
        return render(request, "lista_tarefas/lista.html",{
            "title": lista.nome_descritivo,
            "tarefas": tarefas,
            "lista": lista,
            "perm": booleana,
            "usuario": usuario,
            "nao_convidado": nao_convidado,
            "convites": convites
        })
    except:
        return HttpResponseRedirect(reverse("erro"))

def delete_lista(request, id_lista):
    lista = ListaDeTarefas.objects.get(id_lista=id_lista)
    lista.delete()
    return HttpResponseRedirect(reverse("home"))

# Views de Convite
def criar_convite(request,id_lista,usuario):
    if request.method == 'POST':
        lista = ListaDeTarefas.objects.get(id_lista=id_lista)
        usuario_env = Usuario.objects.get(nome_usuario=usuario)
        try:
            usuario_rec = Usuario.objects.get(nome_usuario=request.POST["valor_selecionado"])
            convite = Convite(fk_nome_usuario_env=usuario_env, fk_nome_usuario_rec=usuario_rec, fk_lista=lista,aceito=0)
            convite.save()
        except:
            pass
        return HttpResponseRedirect(reverse("lista",None,[id_lista]))

def responder_convite(request,id_lista,id_usuario,resposta):
    convite = Convite.objects.get(fk_lista=id_lista,fk_nome_usuario_rec=id_usuario)
    if resposta == 0:
        convite.delete()
    else:
        convite.aceito = 1
        convite.save()
    return HttpResponseRedirect(reverse("home"))

# Views de Tarefa
def criar_tarefa(request,id_lista,texto_tarefa,date):
    lista = ListaDeTarefas.objects.get(id_lista=id_lista)

    timezone_offset = -3.0 
    tzinfo = timezone(timedelta(hours=timezone_offset))
    hora_criacao = datetime.now(tzinfo)
    
    lista.responsavel_modificacao = request.user.nome_usuario
    lista.data_hora_modificacao = hora_criacao
    lista.save()

    tarefa = Tarefas(descricao=texto_tarefa, data_cadastro=hora_criacao, tarefa_concluida=0, fk_lista=lista)
    tarefa.save()

    if date != "-1":
        data_final = datetime.strptime(date, "%Y-%m-%dT%H:%M")
        data_final = data_final.replace(tzinfo=tzinfo)
        tarefa.data_vencimento = date
        tarefa.save()
    data = {
        'success': True,
        'tarefa': {
            "id": tarefa.id_tarefa,
            "descricao": tarefa.descricao,
            "data_cadastro": tarefa.data_cadastro,
            "data_vencimento": tarefa.data_vencimento
        }
    }
    return JsonResponse(data)
    
def att_tarefa(request,id_tarefa,atualizacao,concluida):
    tarefa = Tarefas.objects.get(id_tarefa=id_tarefa)

    lista = ListaDeTarefas.objects.get(id_lista=tarefa.fk_lista.id_lista)
    timezone_offset = -3.0 
    tzinfo = timezone(timedelta(hours=timezone_offset))
    hora_modificacao = datetime.now(tzinfo)
    lista.data_hora_modificacao = hora_modificacao
    lista.save()

    if atualizacao == 1:
        if concluida == 'true':
            tarefa.tarefa_concluida = 1
        if concluida == 'false':
            tarefa.tarefa_concluida = 0
        tarefa.save()
        return JsonResponse({'success': True})
    
    tarefa.delete()

    if len(Tarefas.objects.filter(fk_lista=tarefa.fk_lista.id_lista)) == 0:
        return JsonResponse({'success': False,'vazio': True})

    return JsonResponse({'success': False, 'vazio': False})

def atualizar_tarefa(request, id_tarefa, descricao, date):
    try:
        tarefa = Tarefas.objects.get(id_tarefa=id_tarefa)
        
        lista = ListaDeTarefas.objects.get(id_lista=tarefa.fk_lista.id_lista)
        timezone_offset = -3.0 
        tzinfo = timezone(timedelta(hours=timezone_offset))
        hora_modificacao = datetime.now(tzinfo)
        lista.data_hora_modificacao = hora_modificacao
        lista.save()
        
        tarefa.descricao = descricao
        tarefa.save
    
        
        if date != "-1":
            data_final = datetime.strptime(date, "%Y-%m-%dT%H:%M")
            data_final = data_final.replace(tzinfo=tzinfo)
            tarefa.data_vencimento = data_final
            tarefa.save()
        else :
            tarefa.data_vencimento = None
            tarefa.save()
        
        retorno = {'success': True}
    except:
        retorno = {'success': False}
    
    return JsonResponse(retorno)
        

def pullBancoTarefas(request, id_lista):
    try:
        lista = ListaDeTarefas.objects.get(id_lista=id_lista)
        tarefas = Tarefas.objects.filter(fk_lista=id_lista).order_by("data_cadastro")
        data = {
            "success": "True",
            "tarefas": []
        }
        
        for tarefa in tarefas:
            aux = {}
            aux["id"] = tarefa.id_tarefa
            aux["descricao"] = tarefa.descricao
            aux["data_cadastro"] = tarefa.data_cadastro
            aux["data_vencimento"] = tarefa.data_vencimento
            aux["checked"] = tarefa.tarefa_concluida
            data["tarefas"].append(aux)
    except:
        data = {
            "success": "False",
        }

    return JsonResponse(data)

def pullBancoListas(request):
    try:
        listas = funcoes.listas_usuario(request.user.nome_usuario)
        data = {
            "success": "True", 
            "listas": [],
        }    
        for lista in listas:
            aux = {}
            aux["id"] = lista.id_lista
            aux["texto"] = lista.nome_descritivo
            aux["criacao"] = lista.data_hora_criacao
            aux["modificacao"] = lista.data_hora_modificacao
            aux["responsavel"] = lista.responsavel_modificacao
            data["listas"].append(aux)
    except:
        data = {
            "success": "False",
        }
    
    return JsonResponse(data)

def pullBancoConvites(request):
    convites = Convite.objects.filter(fk_nome_usuario_rec=request.user.nome_usuario,aceito=0)
    data = {
        "convites": [],
    }    
    for convite in convites:
        aux = {}
        aux["nome_lista"] = convite.fk_lista.nome_descritivo
        aux["dono_lista"] = convite.fk_nome_usuario_env.nome_usuario
        aux["id_lista"] = convite.fk_lista.id_lista
        aux["usuario"] = request.user.nome_usuario
        data["convites"].append(aux)
    return JsonResponse(data)

def erro(request):
    return render(request, 'lista_tarefas/erro.html')

def handler404(request, exception):
    return render(request, 'lista_tarefas/404.html', status=404)