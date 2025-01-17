from django.db import models
import datetime


class Article(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(default=datetime.date.today)
    description = models.TextField()

    def __str__(self):
        return self.title