from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    prenom = models.CharField(max_length=15)
    email = models.EmailField(max_length=20)
    phone_number = models.CharField(max_length=20)


    def __str__(self):
        return self.user
