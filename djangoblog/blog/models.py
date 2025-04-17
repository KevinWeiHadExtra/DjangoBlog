from django.db import models

# Create your models here.

class BlogPost(models.Model):
    topic = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    body = models.TextField()
    image = models.ImageField(default = 'fallback.png', blank = True)

    def __str__(self):
        return self.title
    
class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.name