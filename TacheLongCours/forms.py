from django import forms
from .models import Tache, TypeDeTache


class ApplyTach(forms.ModelForm):
    class Meta:
        model = Tache
        fields = '__all__'
        exclude = ['owner']
        widgets = {
            'date_tache': forms.DateInput(format=('%d-%m-%Y'), attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd', 'type': 'date'}),
        }

class AddType(forms.ModelForm):
    class Meta:
        model = TypeDeTache
        fields ='__all__'