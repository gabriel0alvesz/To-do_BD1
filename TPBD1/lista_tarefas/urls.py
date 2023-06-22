from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registrar", views.registrar, name="registrar"),
    path("criar_lista/<str:nome>", views.criar_lista, name="criar_lista"),
    path("lista/<int:id>", views.view_lista, name="lista"),
    path('lista/<int:id>/<int:retorno>/', views.view_lista, name="lista"),
    path('delete_lista/<int:id_lista>', views.delete_lista, name="delete_lista"),
    path("criar_convite/<int:id_lista>/<str:usuario>", views.criar_convite, name="criar_convite"),
    path("criar_tarefa/<int:id_lista>", views.criar_tarefa, name="criar_tarefa"),
    path("att_tarefa/<int:id_tarefa>/<int:atualizacao>", views.att_tarefa, name="att_tarefa"),
    path("responder_convite/<int:id_lista>/<str:id_usuario>/<int:resposta>", views.responder_convite, name="responder_convite"),
]