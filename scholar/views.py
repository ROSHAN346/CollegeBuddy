from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def scholarHome(request):
  return render(request ,'scholar.html')

def login(request):
  return render(request ,'login.html')