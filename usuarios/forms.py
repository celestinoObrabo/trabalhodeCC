from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model

class UserModelForm(forms.ModelForm):
    User._meta.get_field('email').blank = False
    class Meta:
        User = get_user_model()
        fields = ['username','email','password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','maxlength':255, 'placeholder':'Username:'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255,'placeholder':'Email:'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder':'Senha:'}),
        }
        
        error_messages = {
            'username': {
            'required': 'Este campo é obrigatorio'
            },
            'email': {
                'required': 'Este campo é obrigatorio'
            },
            'password': {
                'required': 'Este campo é obrigatorio'
            }
        }

        def save(self, commit=True):
            user = super(UserModelForm, self).save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user
