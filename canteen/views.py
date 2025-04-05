from django.shortcuts import render

# Create your views here.
def canteen(request):
  return render(request ,'canteen.html')