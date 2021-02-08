from django import forms

from .models import Task, Comment, Arquivos


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description','start_date')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content','user')


class UploadForm(forms.ModelForm):
    class Meta:
        model = Arquivos
        fields = ('name', 'arquivo')
