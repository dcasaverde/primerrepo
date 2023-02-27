from django import forms
from .models import libro

class LibroForm(forms.ModelForm):    
    class Meta:
        model = libro
        fields = "__all__" 
        '''fields = ('nombre', 'descripcion')
        widget = {
            'nombre': forms.TextInput(attrs={'class':'form-controls'}),
            'descripcion': forms.Textarea(attrs={'class':'form-controls'}),
        }'''