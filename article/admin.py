from django.contrib import admin
from article.models import Post, Category


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
   list_display = ('title', 'id')
   list_filter = ('category',)


@admin.register(Category)
class CategoryPost(admin.ModelAdmin):
    list_display = ('title', 'id')