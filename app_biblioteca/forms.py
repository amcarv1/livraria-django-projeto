from django import forms

from app_biblioteca.models import Livro

class LivroModelForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = '__all__'