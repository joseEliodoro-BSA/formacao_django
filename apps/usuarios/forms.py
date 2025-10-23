from django import forms


class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome do Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite seu nome aqui..."}
        ),
    )

    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha",
            }
        ),
    )


## Formulário de cadastro
class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome do Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite seu nome aqui..."}
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite seu email"}
        ),
    )

    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha",
            }
        ),
    )

    senha_2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha novamente",
            }
        ),
    )

    # Para validar os campos usando django use "clean_{nome do campo}"
    def clean_nome_cadastro(self):
        nome: str = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if(' ' in nome):
                raise forms.ValidationError("Nome de cadastro não pode ter espaços.")
            return nome
        
        
    def clean_senha_2(self):
        senha_1: str = self.cleaned_data.get("senha_2")
        senha_2: str = self.cleaned_data.get("senha_1") 
        
        if senha_1 != senha_2:
            raise forms.ValidationError("Senhas não são iguais")
        return senha_2