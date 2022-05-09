from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=25, unique=True)

    def __str__(self):
        return f"{self.email}"
