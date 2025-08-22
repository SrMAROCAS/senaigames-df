from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('membro/', views.autentica_membro, name='membro'),
    path('membro/cadastro/', views.cadastro, name='cadastro')
]