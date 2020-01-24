from django.db import models
from django.db.models import CharField

# Create your models here.
class Age(models.Model):
    age = models.CharField(max_length=4)
    def __str__(self):
        return self.age

class Sai(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    agee = models.ForeignKey(Age, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    mob = models.IntegerField()
    mail = models.EmailField(max_length=20)
    image = models.FileField(upload_to='img')
    about = models.CharField(max_length=40)
    def __str__(self):
        return self.fname








