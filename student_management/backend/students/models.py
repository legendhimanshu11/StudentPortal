from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    roll_no = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    attendance = models.IntegerField(default=0)

    def __str__(self):
        return self.username