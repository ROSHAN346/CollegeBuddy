from .models import ItemsInfo
from django.shortcuts import render, redirect
from .forms import LostItemForm
from django.contrib import messages

def report_lost_item(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your lost item report has been submitted successfully!')
            return redirect('report')  # Redirect to the same page or another page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LostItemForm()
    
    return render(request, 'reportLoss.html', {'form': form})

# Create your views here.
def lnfHome(request):
    return render(request, 'lnfHome.html')

def info(request):
    reportInfo = ItemsInfo.objects.all()
    return render(request, 'find.html', { 'info': reportInfo })

def report(request):
    return render(request, 'reportLoss.html')
