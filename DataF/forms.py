from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    modes : Data
    fields = ["Name","Lname", "Email"]
    widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control'})
            'Lname': forms.TextInput(attrs={'class':'form-control'})
            'Email': forms.EmailInput(attrs={'class':'form-control'})
            }
    labels ={
            'Name': 'name',
            'Lname': 'Lname',
            'Email': 'Email',
            }
