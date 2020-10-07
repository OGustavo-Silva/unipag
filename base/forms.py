from django import forms

from .models import Cliente

class PerfilClienteForm(forms.ModelForm):
    razao_social = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Razão social')
    cnpj = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='CNPJ')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='E-mail')
    telefone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Telefone')
    logradouro = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Logradouro')
    numero = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Número')
    bairro = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Bairro')
    cep = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='CEP')
    cidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Cidade')
    uf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='UF')
    complemento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Complemento')

    class Meta:
        model = Cliente
        fields = {'razao_social', 'cnpj', 'email', 'telefone', 'logradouro', 'numero', 'bairro', 'cep', 'cidade', 'uf', 'complemento'}