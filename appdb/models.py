from django.db import models

# Create your models here.
class Db(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(null ='True')


    def __str__(self):
        return self.name 

