from django import forms

class LoginForms(forms.Form):
    nomeLogin = forms.CharField(
        label="name",
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={}
        )
    )
    senhaLogin = forms.CharField(
        label="password",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={}
        )
    )
        

class SignInForms(forms.Form):
    nomeSignIn = forms.CharField(
        label="name",
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={}
        )
    )
    email = forms.EmailField(
        label="email",
        required=True,
        max_length=30,
        widget=forms.EmailInput(
            attrs={}
        )
    )
    senhaSignIn = forms.CharField(
        label="password",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={}
        )
    )
    confirmeSenhaSignIn = forms.CharField(
        label="confirmepassword",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={}
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