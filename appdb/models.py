from django.db import models

# Create your models here.
class Db(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __der__(self):
        return self.name 

