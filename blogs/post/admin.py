from django.contrib import admin
from .models import Category,Comment,Author,Post
# Register your models here.
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)