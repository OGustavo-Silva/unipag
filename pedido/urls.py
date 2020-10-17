from django.urls import path

from . import views

app_name= 'pedido'
urlpatterns = [
    path('visualizarpedido/<id_pedido>' , views.VisualizarPedido.as_view(), name='visualizarpedido'),
]