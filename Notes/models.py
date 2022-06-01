from cgitb import text
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        return f"{self.text[:50]}..."

