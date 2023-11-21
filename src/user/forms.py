from django import forms

class LoginForms(forms.Form):
    nomeLogin = forms.CharField(
        label="Nome de Usuário:",
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-light',
                "style":"background-color: black",
                'id':"form1Example1",
                'placeholder':"Digite seu nome: 'Jóse'"
            }
        )
    )
    senhaLogin = forms.CharField(
        label="Senha:",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control text-light',
                "style":"background-color: black",
                'id':"form1Example2",
                'placeholder':"Digite sua senha: 12345"
            }
        )
    )
        

class SignInForms(forms.Form):
    nomeSignIn = forms.CharField(
        label="Nome:",
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-light',
                'style': 'background-color: black;',
                'id':"form1Example1",
                'placeholder':"Digite seu nome - Ex: 'david'"
            }
        )
    )
    email = forms.EmailField(
        label="E-mail:",
        required=True,
        max_length=30,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control text-light',
                "style":"background-color: black;",
                'id':"form1Example1",
                'placeholder':"Digite seu email - Ex: 'fulano@gmail.com'"
            }
        )
    )
    senhaSignIn = forms.CharField(
        label="Senha:",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control text-light',
                "style":"background-color: black;",
                'id':"form1Example2",
                'placeholder':"Digite sua senha - Ex:1234545"
            }
        )
    )
    confirmeSenhaSignIn = forms.CharField(
        label="Cofirmar Senha:",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control text-light',
                "style":"background-color: black;",
                'id':"form1Example2",
                'placeholder':"Digite sua senha novamente"
            }
        )
    )
    
    def clean_nomeSignIn(self):
        nome = self.cleaned_data.get("nomeSignIn")
    
        nome = nome.capitalize().strip()
        if " " in nome:
            raise forms.ValidationError("Não pode ter espaços!")
        else:
            return None
            
    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        if '@' not in email and '.com' not in email:
            raise forms.ValidationError("Formato do email incorreto")
        else:
            return email
        
    
    def clean_confirmeSenhaSignIn(self):
        senha = self.cleaned_data.get("senhaSignIn")
        senha1 = self.cleaned_data.get("confirmeSenhaSignIn")
        
        if len(senha) < 4 or len(senha1) < 4:
            raise forms.ValidationError("Senha muito pequena!")
        else:
            if senha != senha1:
                raise forms.ValidationError("Senhas não estão iguais")
            else:
                return senha1  