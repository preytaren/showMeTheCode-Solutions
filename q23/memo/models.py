from django.db import models


class MemoModel(models.Model):
    username = models.CharField(max_length=100)
    message = models.TextField()
    time = models.DateTimeField()