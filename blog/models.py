from django.db import models
from django.contrib.auth.models import User
import time

def get_time():
    current_time = time.localtime()
    current_minute = current_time.tm_min
    current_hour = current_time.tm_hour
    current_day = current_time.tm_mday
    current_month = current_time.tm_mon
    current_year = current_time.tm_year
    return f"{current_minute}{current_hour}{current_day}{current_month}{current_year}"

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField( User , on_delete = models.CASCADE )
    name = models.CharField(max_length = 100)
    email_address = models.EmailField()
    phone_number = models.CharField()
    date_joined = models.DateField( auto_now_add = True )
    def __str__(self):
        return self.name

    def save(self , *args , **kwargs):
        super().save(*args , **kwargs)





class Post(models.Model):
    title = models.CharField( max_length = 200 )
    content = models.TextField()
    author = models.ForeignKey( Author , on_delete = models.CASCADE , related_name = "posts" )
    date_posted = models.TimeField()
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey( Post , on_delete = models.CASCADE , related_name = "comments" )
    content = models.TextField(max_length = 10000)
    name = models.CharField(max_length = 100)
    date_posted = models.DateField(auto_now_add = True)
    def __str__(self):
        return f"{self.name}"

class Reply(models.Model):
    comment = models.ForeignKey(Comment , on_delete = models.CASCADE , related_name = "replies")
    name = models.CharField(max_length = 1000)
    content = models.TextField(max_length = 10000)
    date_posted = models.DateField(auto_now_add = True)
    def __str__(self):
        return f"{self.name}"


class Report(models.Model):
    post = models.ForeignKey( Post , on_delete = models.CASCADE , related_name = "reports" )
    reporter = models.CharField(max_length = 100)
    content = models.TextField(max_length = 1000)
    date_reported = models.DateField( auto_now_add = True )
    def __str__(self):
        return f"Report by {self.reporter} on {self.post.title}"
    


class Like(models.Model):
    name = models.ForeignKey( Author , on_delete = models.CASCADE )
    post = models.ForeignKey( Post , on_delete = models.CASCADE )
    date_liked = models.DateField( auto_now_add = True )
    def __str__(self):
        return self.name





