from django.contrib.auth.forms import UserCreationForm
from .models import students

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = students
        exclude = ['created_at']