from django.db import models
from django.contrib.auth.models import User
import time
from .context_processors import get_time #Generates an ID based on current time


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField( User , on_delete = models.CASCADE )
    name = models.CharField(max_length = 100)
    email_address = models.EmailField()
    phone_number = models.CharField()
    date_joined = models.DateField( auto_now_add = True )
    author_id = models.CharField( max_length= 255 , blank = True )
    def __str__(self):
        return self.name

    def save(self , *args , **kwargs):
        if not self.pk:
            current_time = get_time()
            self.author_id = current_time
        super().save(*args , **kwargs)





class Post(models.Model):
    title = models.CharField( max_length = 200 )
    content = models.TextField()
    author = models.ForeignKey( Author , on_delete = models.CASCADE , related_name = "posts" )
    post_id = models.CharField( max_length= 255 , blank= True )
    date_posted = models.TimeField()
    def __str__(self):
        return self.title
    
    def save(self , *args , **kwargs):
        if not self.pk:
            current_time = get_time()
            self.post_id = current_time
        super.save(*args , **kwargs)


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


class About(models.Model):
    about_name = models.CharField( max_length= 255 , default= "about site" )
    about_text = models.TextField( max_length= 10000 )
    about_mission = models.TextField( max_length= 10000 , blank= True )
    about_vision = models.TextField( max_length= 10000 , blank= True )
    date_created = models.DateField( auto_now_add= True )

    def __str__(self):
        return f"About for {self.date_created}"
    
    def save(self , *args , **kwargs):
        super().save( *args , **kwargs )



