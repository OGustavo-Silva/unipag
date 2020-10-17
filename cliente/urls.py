from django.urls import path

from . import views

app_name= 'cliente'
urlpatterns = [
    path('homecliente/', views.HomeCliente.as_view(), name = 'homecliente'),
]