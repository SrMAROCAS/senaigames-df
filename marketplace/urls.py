from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('pinel/', views.pinel, name='pinel')
] 