from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Entry(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    content = RichTextField()
    # content = models.TextField()
