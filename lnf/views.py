from .models import ItemsInfo
from django.shortcuts import render, redirect
from .forms import LostItemForm
from django.contrib import messages

def view_lost_items(request):
    items = ItemsInfo.objects.all().order_by('-created_at')
    return render(request, 'view_items.html', {'items': items})

def report_lost_item(request):
    if request.method == 'POST':
        print("Form submitted!")  # Debug
        print("POST data:", request.POST)  # Debug
        print("FILES data:", request.FILES)  # Debug
        
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")  # Debug
            instance = form.save()
            print("Saved instance ID:", instance.id)  # Debug
            messages.success(request, 'Your lost item report has been submitted successfully!')
            return redirect('ReportChize')  # Use the URL name you defined
        else:
            print("Form errors:", form.errors)  # Debug
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
