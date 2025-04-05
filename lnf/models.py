from django.db import models
from django.utils import timezone

class ItemsInfo(models.Model):
    GATE = [
        ('1', 'GATE NO-1'),
        ('2', 'GATE NO-2'),
    ]
    
    name = models.CharField(max_length=255, default='Title of item')
    image = models.ImageField(upload_to='lost_items/')  # Changed to a more specific path
    email = models.EmailField()
    contact = models.CharField(max_length=15, null=True, blank=True)  # Changed to CharField
    description = models.TextField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)  # Added max_length
    question = models.TextField(max_length=100, null=True, blank=True)  # Fixed null=True
    answer = models.TextField(default='No answer provided')
    gate_no = models.CharField(max_length=1, choices=GATE, default='1')
    created_at = models.DateTimeField(default=timezone.now)  # Added for tracking

    def __str__(self):
        return self.name