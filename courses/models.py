from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    max_students = models.IntegerField()

