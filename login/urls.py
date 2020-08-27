from django.urls import path

from . import views

app_name= 'login'
urlpatterns = [
    path('', views.LogarView.as_view(), name='logar'),
    path('deslogar', views.DeslogarView.as_view(), name='deslogar'),
]