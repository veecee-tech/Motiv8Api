from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display =('id','title', 'content', 'date_posted', 'author')

admin.site.register(BlogPost,BlogPostAdmin)
# Register your models here.
