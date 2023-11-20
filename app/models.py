from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images",default="/user.png")
    bio = models.TextField(null=True,blank=True)

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name  += ' ' + str(self.last_name)
        return name
    
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name




class Post(models.Model):
    headline = models.CharField(max_length=200)
    link = models.URLField(max_length=200,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)
    image = models.ImageField('images',null=True,blank=True,upload_to="images")
    body = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag,null=True)

    def __str__(self):
        return self.headline

class Comment(models.Model):
    auther = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='posts',null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.body
    
    @property
    def created_dynamic(self):
        now = timezone.now()
        return now