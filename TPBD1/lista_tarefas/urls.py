from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('icons/favicon.ico'))),
    path('', views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registrar", views.registrar, name="registrar"),
    path("criar_lista/<str:nome>", views.criar_lista, name="criar_lista"),
    path("lista/<int:id>", views.view_lista, name="lista"),
    path('delete_lista/<int:id_lista>', views.delete_lista, name="delete_lista"),
    path("criar_convite/<int:id_lista>/<str:usuario>", views.criar_convite, name="criar_convite"),
    path("criar_tarefa/<int:id_lista>/<str:texto_tarefa>/<str:date>", views.criar_tarefa, name="criar_tarefa"),
    path("att_tarefa/<int:id_tarefa>/<int:atualizacao>", views.att_tarefa, name="att_tarefa"),
    path("responder_convite/<int:id_lista>/<str:id_usuario>/<int:resposta>", views.responder_convite, name="responder_convite"),
    path("pullBancoTarefas/<int:id_lista>", views.pullBancoTarefas, name="pullBancoTarefas"),
    path("pullBancoListas", views.pullBancoListas, name="pullBancoListas"),
    path("pullBancoConvites", views.pullBancoConvites, name="pullBancoConvites"),
    path("erro", views.erro, name="erro"),
]