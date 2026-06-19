from django import forms
from .models import Lecturer


class LecturerForm(forms.ModelForm):

    class Meta:
        model = Lecturer

        fields = [
            'user'
        ]
