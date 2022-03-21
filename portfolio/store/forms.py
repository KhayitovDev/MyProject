from django.forms import ModelForm
from .models import contactPage
from django import forms


class Contact(ModelForm):
    class Meta:
        model = contactPage
        fields = ('name','email', 'message')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'})
        }
