from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    date_published = models.DateTimeField(auto_now=False)


    def __str__(self) -> str:
        return self.title
