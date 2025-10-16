from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
       label= "Nome do Login", 
       required= True,
       max_length= 100,
       widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite seu nome aqui..."
            }
        ),
    )

    senha = forms.CharField(
        label= "Senha", 
        required= True,
        max_length= 70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )


## Formulário de cadastro
class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
       label= "Nome do Cadastro", 
       required= True,
       max_length= 100,
       widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite seu nome aqui..."
            }
        ),
    )
    nome_email = forms.EmailField(
       label= "Email", 
       required= True,
       max_length= 100,
       widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite seu email"
            }
        ),
    )

    senha_1 = forms.CharField(
        label= "Senha", 
        required= True,
        max_length= 70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )

    senha_2 = forms.CharField(
        label= "Confirme sua senha", 
        required= True,
        max_length= 70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',
            }
        ),
    )