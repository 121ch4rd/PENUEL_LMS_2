from django.shortcuts import render
from django.shortcuts import redirect
from students.models import Student
from .models import Result
from .utils import calculate_gpa

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from students.models import Student
from .forms import ResultForm

def upload_result(request):
    form = ResultForm()
    if request.method == 'POST':
        form = ResultForm(
            request.POST
        )
        if form.is_valid():
            form.save()
            return redirect(
                'lecturer_dashboard'
            )
    return render(
        request,
        'results/upload_result.html',
        {'form': form}
    )
    
def student_results(request):
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
        (
            semester1_gpa +
            semester2_gpa
        ) / 2,
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
        overall_gpa,
    }
    return render(
        request,
        'results/student_results.html',
        context
    )

def download_result_pdf(request):
    student = Student.objects.get(
        user=request.user
    )
    response = HttpResponse(
        content_type='application/pdf'
    )
    response[
        'Content-Disposition'
    ] = (
        'attachment; '
        'filename="result.pdf"'
    )
    p = canvas.Canvas(response)
    p.drawString(
        100,
        800,
        "PENUEL LMS_2"
    )
    p.drawString(
        100,
        780,
        f"Name: {student.name}"
    )
    p.drawString(
        100,
        760,
        f"Reg No: {student.reg_no}"
    )
    y = 720
    results = Result.objects.filter(
        student=student
    )
    for result in results:
        p.drawString(
            100,
            y,
            f"{result.subject.name}"
        )
        p.drawString(
            250,
            y,
            f"{result.total_mark}"
        )
        p.drawString(
            350,
            y,
            f"{result.grade}"
        )
        y -= 20
    p.save()
    return response
