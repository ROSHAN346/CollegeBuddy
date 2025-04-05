from django import forms
from .models import ItemsInfo

class LostItemForm(forms.ModelForm):
    class Meta:
        model = ItemsInfo
        exclude = ['created_at']