from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    reg_no = models.CharField(
        max_length=50,
        unique=True
    )

    program = models.CharField(
        max_length=100
    )

    year_of_study = models.IntegerField()

    def __str__(self):
        return (
            self.user.get_full_name()
        )
