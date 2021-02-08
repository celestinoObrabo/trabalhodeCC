from django import forms
from .models import Encontros


class DateInput(forms.DateInput):
    input_type = 'date'


class EncontrosForms(forms.ModelForm):

    class Meta:
        model = Encontros
        widgets = {
            'start_date': DateInput()
        }
        fields = ('titulo', 'descricao', 'start_date')