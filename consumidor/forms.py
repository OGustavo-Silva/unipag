from django import forms
from .models import Consumidor

class CadastroConsumidorForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = ['nome', 'sobrenome', 'email', 'senha', 'cpf', 'nascimento', 'sexo', 'logradouro', 'numero', 'bairro',
                  'cep', 'cidade', 'uf', 'complemento', 'telefone', 'nacionalidade', 'numero_cartao',
                  'codigo_seguranca', 'titular_cartao', 'validade_cartao', 'limite_compra']
        widgets = {
            'senha': forms.PasswordInput()
        }

class PerfilConsumidorForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Nome')
    sobrenome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Sobrenome')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'E-mail')
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'CPF')
    nascimento = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Data nascimento')
    logradouro = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Logradouro')
    numero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Número')
    bairro = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Bairro')
    cep = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'CEP')
    cidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Cidade')
    uf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'UF')
    complemento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Complemento')
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Telefone')
    nacionalidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Nacionalidade')
    numero_cartao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Número do cartão')
    codigo_seguranca = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Código de segurança')
    titular_cartao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Nome como no cartão')
    validade_cartao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Validade')
    limite_compra = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}), label = 'Limite de compra no UNIPAG')

    class Meta:
        model = Consumidor
        fields = {'nome', 'sobrenome', 'email', 'cpf', 'nascimento', 'logradouro', 'numero', 'bairro', 'cep', 'cidade',
                    'uf', 'complemento', 'telefone', 'nacionalidade', 'numero_cartao', 'codigo_seguranca','titular_cartao',
                    'validade_cartao', 'limite_compra'}