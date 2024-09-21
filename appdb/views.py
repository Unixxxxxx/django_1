from django.shortcuts import render
from django.http import HttpResponse 
from .forms import DbForm
from .models import Db  

# Create your views here.
def home(request):
    return render (request, 'home.html')

def Db(request):
    if request.method == 'POST':
        form = DbForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            form.save()
            return HttpResponse("The data is save in DB.")
        else:
            form = DbForm()
    return render (request, 'DB/form.html',{'form': form})

