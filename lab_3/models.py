from django.db import models

class Diary(models.Model):
    date = models.DateTimeField()
    activity = models.TextField(max_length=60)
