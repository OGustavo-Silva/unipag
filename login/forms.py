from django import forms

from base.models import Cliente, Consumidor

class ClienteLoginForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("email", "senha")