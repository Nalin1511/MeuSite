from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastroUsuarioForm(UserCreationForm):

    first_name = forms.CharField(label = 'Primeiro Nome', max_length=50, required=True, help_text='Campo de nome obrigatório')
    last_name = forms.CharField(label = 'ultimo Nome', max_length=50, required=True, help_text='obrigatório')
    email = forms.EmailField (label = 'E-mail', max_length=50,  help_text='Por favor informe um e-mail válido' )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']