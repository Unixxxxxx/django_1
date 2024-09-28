from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'lname', 'email']
        
        # Adding widgets to style the form using Tailwind CSS or any other classes
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'placeholder': 'First Name'
            }),
            'lname': forms.TextInput(attrs={
                'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'placeholder': 'Email Address'
            }),
        }
        
        labels = {
            'name': 'First Name',
            'lname': 'Last Name',
            'email': 'Email Address',
        }

