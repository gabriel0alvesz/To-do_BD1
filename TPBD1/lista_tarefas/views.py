from django.shortcuts import render
from django.db import IntegrityError
from .models import Usuario, Tarefas, ListaDeTarefas, Convite
from django.contrib.auth import authenticate, login, logout # Utilizados para autenticar usuário
from django.http import HttpResponseRedirect 
from django.urls import reverse

# Create your views here.

def home(request):

    usuarios = len(Usuario.objects.all())
    listas   = len(ListaDeTarefas.objects.all())
    tarefas  = len(Tarefas.objects.all())

    if request.user.is_authenticated:
        usuario = request.user


    return render(request, "lista_tarefas/home.html", {
        "title": "Home",
        "usuario": usuario,
        "usuarios": usuarios,
        "listas": listas,
        "tarefas": tarefas,
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
            return render(request, "lista_tarefas/register.html", {
                "title": "Registrar",
                "message": "Senhas diferentes."
            })

        # Attempt to create new user
        try:
            user = Usuario.objects.create_user(nome_usuario, password, email, nome, telefone)
            user.save()
        except ValueError as e:
            return render(request, "lista_tarefas/register.html", {
                "title": "Registrar",
                "message": e,
            })
        except IntegrityError:
            return render(request, "lista_tarefas/register.html", {
                "title": "Registrar",
                "message": "Usuário já utilizado."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "lista_tarefas/register.html",{
            "title": "Register"
        })