from django.shortcuts import render
from django.shortcuts import redirect

from .forms import LecturerForm


def add_lecturer(request):

    form = LecturerForm()

    if request.method == 'POST':

        form = LecturerForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'admin_dashboard'
            )

    return render(
        request,
        'lecturers/add_lecturer.html',
        {'form': form}
    )
