from django.db import models

# Create your models here.
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    class Meta:
       verbose_name = "Books"
       verbose_name_plural = "Books"

    def __str__(self):
        return self.title