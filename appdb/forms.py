from django import forms
from .models import Db

class DbForm(forms.ModelForm):
    class Meta:
        model = Db
        fields =['name','age', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            }
        labels  ={
                'name': 'name ',
                'age': 'age',
                'email': 'email'
                }
