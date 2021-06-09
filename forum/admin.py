from django.contrib import admin
from .models import Category, Posts, LikeDislike, Comments, Statistics

admin.site.register(Category)
admin.site.register(Posts)
admin.site.register(LikeDislike)
admin.site.register(Comments)
admin.site.register(Statistics)
