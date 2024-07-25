from django.db import models

# Create your models here.


class Postion(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Employee(models.Model):
    ful_name = models.CharField(max_length=50)
    emo_code = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    postion = models.ForeignKey(Postion, on_delete=models.CASCADE)  

    def __str__(self):
        return self.ful_name