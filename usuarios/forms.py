from django import forms
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    username = forms.CharField(
        label="Nome do Usuario",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class":"form-control",
            "placeholder":"Usuario"}
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"class":"form-control",
            "placeholder":"Senha"}
        )
    )

class CadastroForm(forms.Form):
    nome = forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class":"form-control",
            "placeholder":"nome",
            }
        )
    )
    sobrenome = forms.CharField(
    label="Sobrenome",
    required=True,
    max_length=100,
    widget=forms.TextInput(
        attrs={"class":"form-control",
        "placeholder":"Sobrenome"}
    )
    )
    email = forms.EmailField(
    label="Email",
    required=True,
    max_length=100,
    widget=forms.EmailInput(
        attrs={"class":"form-control",
        "placeholder":"Email ex:'Jao_paz@aptx.com'"}
    )
)
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"class":"form-control",
            "placeholder":"Senha"}
        )
    )
    senha_2 = forms.CharField(
    label="Digite novamente",
    required=True,
    max_length=100,
    widget=forms.PasswordInput(
        attrs={"class":"form-control",
        "placeholder":"Repetir senha"}
    )
)
    username = forms.CharField(
    label="Usuario",
    required=True,
    max_length=100,
    widget=forms.TextInput(
        attrs={"class":"form-control",
        "placeholder":"Usuario *Nome do usuario que voçe irar utlizar para acessar o site*"}
    )
)

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if nome:
            if any( x.isdigit() for x in nome):
                raise forms.ValidationError('nome nao pode conter numeros')                  
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços nao sao permitidos nesse campo')
          
            else:
                return nome.lower()

    def clean_sobrenome(self):
        sobrenome = self.cleaned_data.get('sobrenome')
        if sobrenome:
            if any( x.isdigit() for x in sobrenome):
                raise forms.ValidationError('sobrenome nao pode conter numeros')                 
            else:
                sobrenome = sobrenome.strip()
                return sobrenome.lower()
          



    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email já utilizado')
            else:
                return email
        

    def clean_senha_1(self):
        senha_1 = self.cleaned_data.get('senha_1')
        if senha_1 :
            senha_1 = senha_1.strip()
            if ' ' in senha_1:
                raise forms.ValidationError('Espaços nao sao permitidos nesse campo')            
            if len(senha_1)<=6: #verificando tamanho
                raise forms.ValidationError('Senha muito curta')
            if not any(x.isupper() for x in senha_1 ): #verficando contem letras Maiscula
                raise forms.ValidationError('Precisa conter pelo 1 letra Maisculo')
            if not any(x.islower() for x in senha_1 ):#verficando contem letras Minuscula
                raise forms.ValidationError('Precisa conter pelo 1 letra Minusculo')
            if not any(x.isdigit() for x in senha_1 ):#verficando contem numeros
                raise forms.ValidationError('Precisa conter 1 Numero')
            else:
                return senha_1
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')
        
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas nao sao iguais')
            else:
                return senha_1

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            username = username.lower()
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('Usuario já utilizado')
            else:
                return username
           