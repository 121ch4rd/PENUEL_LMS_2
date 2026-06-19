from django.db import models
from django.contrib.auth.models import User


class Lecturer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            self.user.get_full_name()
        )
