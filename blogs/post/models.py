from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    pub_date = models.DateField( auto_now_add=True)
    categories =models.ManyToManyField(Category)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post/", null=True, blank=True , height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.content}"
