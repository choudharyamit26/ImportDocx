from django import forms
from .models import Questions



class Importdataform(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'