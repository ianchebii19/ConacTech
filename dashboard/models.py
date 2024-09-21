from django.db import models
from django.contrib.auth.models import User # type: ignore

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    

class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    title = models.CharField(max_length=255
                            )
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Todo(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     title = models.CharField(max_length=255                       )
     is_finished = models.BooleanField(default = False)

     def __str__(self):
        return self.title