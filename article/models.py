from django.db import models
from django.utils.text import slugify
from transliterate import translit
from django.urls import reverse



class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)


    def __str__(self) -> str:
        return f'{self.title}'

    def save(self, *args, **kwargs):
        test = self.title
        test_1 = translit(test, language_code='ru', reversed=True)
        test_1 = test_1.strip().split(" ")
        test_1 = "-".join(test_1)
        self.slug = slugify(test_1)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article:PostListView', kwargs={'category_slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category_posts')
    content = models.TextField(max_length=1000, null=True)
    is_visible = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('article:PostDetailView', kwargs={'category_slug': self.category.slug, 'id_post': self.id})
    




