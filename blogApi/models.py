from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.



class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=User)
   
 
