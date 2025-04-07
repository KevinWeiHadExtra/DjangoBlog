from django.db import models

# Create your models here.

class BlogPost(models.Model):
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    body = models.TextField()

    def __str__(self):
        return self.description