from django.db import models

# Create your models here.


class Task(models.Model):
    detail = models.CharField(max_length=150)
    creation_date = models.DateTimeField(auto_now = True)


class Todo(models.Model):
    tasks = models.ManyToManyField(Task, related_name="liste")

