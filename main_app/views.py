from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Define the home view
def home(request):
  return render(request, 'home.html')

@login_required
def about(request):
  return render(request, 'about.html')

def accounts(request):
  return render(request, 'registration/login.html')

    