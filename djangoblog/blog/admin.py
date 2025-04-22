from django.contrib import admin
from .models import BlogPost,Message,Rating
# Register your models here.

class RatingInLine(admin.StackedInline):
    model = Rating


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["topic"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [RatingInLine]


admin.site.register(BlogPost, PostAdmin)
admin.site.register(Message)