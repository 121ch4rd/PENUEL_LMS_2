from django.db import models
from students.models import Student
from subjects.models import Subject

def calculate_grade(total):

    if total >= 70:
        return "A", 5.0

    elif total >= 60:
        return "B+", 4.0

    elif total >= 50:
        return "B", 3.0

    elif total >= 40:
        return "C", 2.0

    else:
        return "F", 0.0

class Result(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    assignment_mark = models.FloatField()
    exam_mark = models.FloatField()
    total_mark = models.FloatField(
        blank=True,
        null=True
    )
    grade = models.CharField(
        max_length=5,
        blank=True
    )
    grade_point = models.FloatField(
        blank=True,
        null=True
    )
    def save(self,*args,**kwargs):
        if self.assignment_mark < 0:
            raise ValueError(
            "Assignment cannot be negative"
            )
        if self.exam_mark < 0:
            raise ValueError(
            "Exam cannot be negative"
            )
        if self.assignment_mark > 30:
            raise ValueError(
            "Assignment max is 30"
            )
        if self.exam_mark > 70:
            raise ValueError(
            "Exam max is 70"
            )
        self.total_mark = (
            self.assignment_mark +
            self.exam_mark
        )

        self.grade,self.grade_point = (
            calculate_grade(
            self.total_mark
            )
        )

        super().save(
             *args,
             **kwargs
        )
