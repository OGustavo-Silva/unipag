from django.urls import path

from . import views

app_name='consumidor'
urlpatterns = [
    path('homeconsumidor/', views.homeConsumidor.as_view(), name='homeconsumidor'),
]