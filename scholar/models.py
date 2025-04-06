from django.db import models

class students(models.Model):
    CATEGORY = [
        ('1', 'GENERAL'),
        ('2', 'OBC'),
        ('3', 'SC'),
        ('4', 'ST'),
        ('5', 'PWD'),
    ]
    GENDER = [
        ('1' , 'Male'),
        ('2' , 'Female'),
    ]
    EDUCATION = [
        ('1' , 'High School'),
        ('2' , 'Intermidiate'),
        ('3' , 'UG'),
        ('4' , 'PG'),
        ('5' , 'PhD'),
    ]
    COURSE = [
        ('1' , 'High School'),
        ('2' , 'Intermidiate'),
        ('3' , 'UG'),
        ('4' , 'PG'),
        ('5' , 'PhD'),
    ]
    name = models.CharField(max_length=255, default='name')
    email = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    institution = models.CharField(max_length=255, null=True, blank=True)
    gpa = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='1')
    category = models.CharField(max_length=1, choices=CATEGORY, default='1')
    education = models.CharField(max_length=1, choices=EDUCATION, default='1')
    courses = models.CharField(max_length=1, choices=COURSE, default='1')
    dob = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
