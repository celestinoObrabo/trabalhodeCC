from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Orientacao,Categoria,Curso,User


class OrientForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.SelectMultiple)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control col-md-7 col-xs-12', 'weight': '50%'}))
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control col-md-7 col-xs-12', 'weight': '50%'}))
    class Meta:
        model = Orientacao
        fields = ('name', 'description', 'categoria', 'curso', 'user')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
