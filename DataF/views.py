from django.shortcuts import render, redirect
from .forms import DataForm

# Create your views here.
def data_view(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = DataForm()  # Display an empty form for GET request
    
    return render(request, "Data/index.html", {'form': form})
def success_view(request):
    return render(request, "Data/success.html") 
