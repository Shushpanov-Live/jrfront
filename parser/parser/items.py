# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
import scrapy
from article.models import Category, Post


class CategoryItem(DjangoItem):
    django_model = Category

class PostItem(DjangoItem):
    django_model = Post
    category_title = scrapy.Field()