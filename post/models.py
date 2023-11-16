from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100, default='user')
    avatar = models.ImageField(upload_to='post/static/images/', blank=True)
    title = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='post/static/images/', blank=True)
    pictur2 = models.ImageField(upload_to='post/static/images/', null=True, blank=True)
    text = models.TextField(blank=True)
    
    def __str__(self):
        return self.name