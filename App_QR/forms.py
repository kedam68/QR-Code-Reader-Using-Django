from django import forms 
from .models import *
  
class QRForm(forms.ModelForm): 
    class Meta: 
        model = QR
        fields = ['image'] 