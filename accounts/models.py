from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    A user model for maintaining premium
    status and login information
    """
    # add additional fields in here
    premium = models.BooleanField(default=False)

    def __str__(self):
        return self.email
