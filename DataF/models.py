from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} {self.lname}"


