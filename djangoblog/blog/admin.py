from django.contrib import admin
from .models import BlogPost,Message,Rating,Comment
# Register your models here.

class RatingInLine(admin.StackedInline):
    model = Rating

class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [RatingInLine, CommentInLine]


admin.site.register(BlogPost, PostAdmin)
admin.site.register(Message)