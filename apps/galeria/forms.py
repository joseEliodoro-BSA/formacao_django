from django import forms  
from apps.galeria.models import Fotografia

# Para não precisar criar um formulário do zero, o django pode criar formulários apartir dos nossos models
# Então podemos usar a seguinte forma para criar formulários com base em um model já criado.
class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada', ]
        widgets = {
            "nome": forms.TextInput(attrs={"class":'form-control'}), 
            "legenda": forms.TextInput(attrs={"class":'form-control'}), 
            "categoria": forms.Select(attrs={"class":'form-control'}), 
            "descricao": forms.Textarea(attrs={"class":'form-control'}), 
            "foto": forms.FileInput(attrs={"class":'form-control'}), 
            "data_fotografia": forms.DateInput(
                format= "%d/%m/%Y",
                attrs={
                    "type": 'date',
                    "class":'form-control'
                }
            ), 
            "usuario": forms.Select(attrs={"class":'form-control'}), 
        }