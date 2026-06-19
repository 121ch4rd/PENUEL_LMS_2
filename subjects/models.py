from django.db import models
from lecturers.models import Lecturer


class Subject(models.Model):

    SEMESTER_CHOICES = (
        (1, "Semester 1"),
        (2, "Semester 2"),
    )

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    credit_hours = models.IntegerField()

    semester = models.IntegerField(
        choices=SEMESTER_CHOICES
    )

    lecturer = models.ForeignKey(
        Lecturer,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.code} - {self.name}"
