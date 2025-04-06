from django.shortcuts import render , redirect
from .forms import StudentRegistrationForm
from django.contrib import messages
from .models import students
from datetime import datetime
import random

def scholarHome(request):
  return render(request ,'scholar.html')

def login(request):
  return render(request ,'login.html')

def saveToDB(request):
    if request.method == 'POST':
        print("Form submitted!") 
        print("POST data:", request.POST) 
        
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            instance = form.save()
            print("Saved instance ID:", instance.id) 
            messages.success(request, 'Your lost item report has been submitted successfully!')
            return redirect('dash')  
        else:
            print("Form errors:", form.errors)  
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentRegistrationForm()
    return render(request, 'login.html', {'form': form})


students = [
    {
        'id': 1,
        'name': 'Chad',
        'email': 'ji@dhrit.gmail.com',
        'description': 'A passionate web dev',
        'institution': 'DTU',
        'gpa': '7.5',
        'gender': 'Male',
        'category': 'General',
        'education': 'Intermediate',
        'courses': 'BTech',
        'dob': '22/08/2003'
    },
    {
        'id': 2,
        'name': 'Aryan',
        'email': 'aryan@abc.com',
        'description': 'AI enthusiast and coder',
        'institution': 'IIT Delhi',
        'gpa': '9.1',
        'gender': 'Male',
        'category': 'OBC',
        'education': 'UG',
        'courses': 'BTech',
        'dob': '14/07/2002'
    },
    {
        'id': 3,
        'name': 'Priya',
        'email': 'priya123@gmail.com',
        'description': 'Loves data science',
        'institution': 'IIT Bombay',
        'gpa': '8.7',
        'gender': 'Female',
        'category': 'General',
        'education': 'PG',
        'courses': 'MTech',
        'dob': '05/11/2000'
    },
    {
        'id': 4,
        'name': 'Ravi',
        'email': 'ravi_kumar@xyz.com',
        'description': 'Competitive programmer',
        'institution': 'NIT Trichy',
        'gpa': '8.0',
        'gender': 'Male',
        'category': 'SC',
        'education': 'UG',
        'courses': 'BTech',
        'dob': '20/02/2002'
    },
    {
        'id': 5,
        'name': 'Sneha',
        'email': 'sneha.dev@gmail.com',
        'description': 'Frontend designer',
        'institution': 'BITS Pilani',
        'gpa': '9.3',
        'gender': 'Female',
        'category': 'General',
        'education': 'UG',
        'courses': 'BTech',
        'dob': '03/09/2001'
    },
    {
        'id': 6,
        'name': 'Imran',
        'email': 'imran@codeverse.com',
        'description': 'Backend expert',
        'institution': 'IIIT Hyderabad',
        'gpa': '8.5',
        'gender': 'Male',
        'category': 'OBC',
        'education': 'UG',
        'courses': 'BTech',
        'dob': '11/06/2002'
    },
    {
        'id': 7,
        'name': 'Kavya',
        'email': 'kavya@mlguru.ai',
        'description': 'Machine learning wizard',
        'institution': 'IIT Kanpur',
        'gpa': '9.0',
        'gender': 'Female',
        'category': 'ST',
        'education': 'PG',
        'courses': 'MTech',
        'dob': '29/01/2000'
    },
    {
        'id': 8,
        'name': 'Aman',
        'email': 'aman.cs@gmail.com',
        'description': 'Full-stack engineer',
        'institution': 'NSUT',
        'gpa': '7.8',
        'gender': 'Male',
        'category': 'General',
        'education': 'UG',
        'courses': 'BTech',
        'dob': '16/10/2001'
    },
    {
        'id': 9,
        'name': 'Neha',
        'email': 'neha.tech@outlook.com',
        'description': 'Database lover',
        'institution': 'JNU',
        'gpa': '8.9',
        'gender': 'Female',
        'category': 'PWD',
        'education': 'PhD',
        'courses': 'PhD',
        'dob': '12/12/1998'
    },
    {
        'id': 10,
        'name': 'Varun',
        'email': 'varun@coderhub.org',
        'description': 'Cybersecurity researcher',
        'institution': 'IISc Bangalore',
        'gpa': '9.6',
        'gender': 'Male',
        'category': 'General',
        'education': 'PhD',
        'courses': 'PhD',
        'dob': '07/04/1997'
    }
]


def renderPage(request):
    student = random.choice(students)
    scholarships = [
        {
            'id': 1,
            'name': 'National Merit Scholarship',
            'amount': '$5,000',
            'deadline': datetime(2025, 6, 30),
            'description': 'Prestigious scholarship for outstanding academic achievement and leadership potential.',
            'criteria': ['GPA > 3.5', 'Academic Excellence', 'Leadership Skills'],
            'matched': 'gpa' in student and float(student['gpa']) > 7.5,
        },
        {
            'id': 2,
            'name': 'Engineering Excellence Award',
            'amount': '$3,000',
            'deadline': datetime(2025, 5, 15),
            'description': 'For students pursuing undergraduate studies in engineering with proven technical skills.',
            'criteria': ['Engineering Major', 'Technical Projects', 'Innovation'],
            'matched': 'courses' == '3' or 'BTech' in student['courses'],
        },
        {
            'id': 3,
            'name': f'{student['category']} Student Support Grant',
            'amount': '$2,500',
            'deadline': datetime(2025, 7, 10),
            'description': f'Support for students from {student['category']} category to pursue higher education.',
            'criteria': [student['category'], 'Financial Need', 'Academic Potential'],
            'matched': True,  # Always matched since it's based on their category
        },
        {
            'id': 4,
            'name': 'Women in STEM Scholarship',
            'amount': '$4,000',
            'deadline': datetime(2025, 5, 31),
            'description': 'Supporting female students pursuing careers in Science, Technology, Engineering, and Mathematics.',
            'criteria': ['Female', 'STEM Field', 'Research Interest'],
            'matched': 'gender' == 'Female' and student['education'] in ['PhD', 'Intermediate', 'UG'],
        },
        {
            'id': 5,
            'name': 'Graduate Research Fellowship',
            'amount': '$6,000',
            'deadline': datetime(2025, 4, 30),
            'description': 'For graduate students pursuing original research in their field of study.',
            'criteria': ['Graduate Level', 'Research Proposal', 'Academic Excellence'],
            'matched': 'education' in ['UG', 'PG'],
        },
    ]
    scholarships = [s for s in scholarships if s.get('matched', False)]
    
    
    return render(request, 'page.html', {'student': student , 'scholarships' : scholarships})