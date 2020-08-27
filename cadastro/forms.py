from django import forms
from base.models import Cliente, Consumidor

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['email', 'senha', 'razao_social', 'cnpj', 'telefone', 'logradouro', 'numero', 'bairro',
                  'cep', 'cidade', 'uf', 'complemento']
        widgets = {
            'senha': forms.PasswordInput()
        }

class ConsumidorForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = ['nome', 'sobrenome', 'email', 'senha', 'cpf', 'nascimento', 'sexo', 'logradouro', 'numero', 'bairro',
                  'cep', 'cidade', 'uf', 'complemento', 'telefone', 'nacionalidade', 'numero_cartao',
                  'codigo_seguranca', 'titular_cartao', 'validade_cartao', 'limite_compra']
        widgets = {
            'senha': forms.PasswordInput()
        }