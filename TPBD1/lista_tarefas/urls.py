from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registrar", views.registrar, name="registrar"),
    path("criar_lista", views.criar_lista, name="criar_lista"),
    path("lista/<int:id>", views.lista, name="lista"),
    path("criar_convite", views.criar_convite, name="criar_convite"),
]