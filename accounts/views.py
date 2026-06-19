from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import LoginForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required

from students.models import Student
from lecturers.models import Lecturer
from subjects.models import Subject
from results.models import Result
from results.forms import ResultForm
from results.utils import calculate_gpa

def login_view(request):

    form = LoginForm()

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            profile = UserProfile.objects.get(
                user=user
            )

            if profile.role == "ADMIN":
                return redirect(
                    'admin_dashboard'
                )

            elif profile.role == "LECTURER":
                return redirect(
                    'lecturer_dashboard'
                )

            else:
                return redirect(
                    'student_dashboard'
                )

    return render(
        request,
        'login.html',
        {'form': form}
    )

def logout_view(request):

    logout(request)

    return redirect('login')

@login_required
def admin_dashboard(request):
    context = {
        "students":
        Student.objects.count(),

        "lecturers":
        Lecturer.objects.count(),

        "subjects":
        Subject.objects.count(),

        "results":
        Result.objects.count(),
    }
    return render(
        request,
        "admin_dashboard.html",
        context
    )

@login_required
def lecturer_dashboard(request):
    form = ResultForm()
    if request.method == "POST":
        form = ResultForm(
            request.POST
        )
        if form.is_valid():

            form.save()
    return render(
        request,
        "lecturer_dashboard.html",
        {
            "form": form
        }
    )

@login_required
def student_dashboard(request):
    student = Student.objects.get(
        user=request.user
    )
    semester1_results = Result.objects.filter(
        student=student,
        subject__semester=1
    )
    semester2_results = Result.objects.filter(
        student=student,
        subject__semester=2
    )
    semester1_gpa = calculate_gpa(
        student,
        1
    )
    semester2_gpa = calculate_gpa(
        student,
        2
    )
    overall_gpa = round(
        (semester1_gpa +
        semester2_gpa) / 2,
        2
    )
    context = {
        'student': student,
        'semester1_results':
            semester1_results,
        'semester2_results':
            semester2_results,
        'semester1_gpa':
            semester1_gpa,
        'semester2_gpa':
            semester2_gpa,
        'overall_gpa':
            overall_gpa
    }
    return render(
        request,
        'student_dashboard.html',
        context
    )