from django.db import models

# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    userid = models.IntegerField()

    
