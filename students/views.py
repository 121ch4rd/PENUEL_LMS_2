from django.shortcuts import render
from django.shortcuts import redirect
from .models import Student

from .forms import StudentForm

def add_student(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(
            request.POST
        )
        if form.is_valid():
            form.save()
            return redirect(
                'admin_dashboard'
            )
    return render(
        request,
        'students/add_student.html',
        {'form': form}
    )

def student_list(request):
    query = request.GET.get('q')
    students = Student.objects.all()
    if query:
        students = students.filter(
            name__icontains=query
        )
    return render(
        request,
        'students/student_list.html',
        {
            'students': students
        }
    )

def edit_student(request,id):
    student = Student.objects.get(
        id=id
    )
    form = StudentForm(
        instance=student
    )
    if request.method == "POST":
        form = StudentForm(
            request.POST,
            instance=student
        )
        if form.is_valid():
            form.save()
            return redirect(
                'student_list'
            )
    return render(
        request,
        'students/edit_student.html',
        {'form':form}
    )

def delete_student(request,id):
    student = Student.objects.get(
        id=id
    )
    student.delete()
    return redirect(
        'student_list'
    )
