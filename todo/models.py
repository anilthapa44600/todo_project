from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ToDo(models.Model):
    text = models.CharField(max_length=255)
    added_date = models.DateTimeField()
    priority = models.CharField(max_length=10, default='normal')
    status = models.CharField(max_length=1, default='0')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
