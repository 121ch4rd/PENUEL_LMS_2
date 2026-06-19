from django import forms
from .models import Result


class ResultForm(forms.ModelForm):

    class Meta:
        model = Result

        fields = [
            'student',
            'subject',
            'assignment_mark',
            'exam_mark'
        ]
