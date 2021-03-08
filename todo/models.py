from django.db import models

# Create your models here.


class ToDo(models.Model):
    text = models.CharField(max_length=255)
    added_date = models.DateTimeField()

    def __str__(self):
        return self.text