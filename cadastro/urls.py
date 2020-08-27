from django.urls import path

from . import views

app_name= 'cadastro'
urlpatterns = [
    path('cadastrarcliente/', views.CadastrarCliente.as_view(), name = 'cadastrarcliente'),
    path('cadastrarconsumidor/', views.CadastrarConsumidor.as_view(), name = 'cadastrarconsumidor'),
]