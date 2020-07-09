from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Contact(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    message = models.TextField()
    approved = models.BooleanField(default=False)

    @property
    def status(self):
        if self.approved == True:
            return "Approved"
        else:
            return "Not approved"

    def __str__(self):
        return self.email

