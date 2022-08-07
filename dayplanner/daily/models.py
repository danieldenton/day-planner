from django.db import models

# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Task(models.Model):
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

