from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=500,unique=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return  f"{self.email}"