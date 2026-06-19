from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SubjectForm


def add_subject(request):

    form = SubjectForm()

    if request.method == 'POST':

        form = SubjectForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'admin_dashboard'
            )

    return render(
        request,
        'subjects/add_subject.html',
        {'form': form}
    )
