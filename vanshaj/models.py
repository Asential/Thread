from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Individual(models.Model):
    person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    significantOther = models.OneToOneField('self', null=True, on_delete=models.SET_NULL, blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    children = models.ManyToManyField('self', blank=True, symmetrical=False, related_name="child")

    def __str__(self):
        return f"{self.person}"