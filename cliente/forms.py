from django import forms
from .models import Cliente
from .models import Ventas



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields= '__all__'
   
class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields= '__all__'     
        
        