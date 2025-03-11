from django.db import models
from django.contrib.auth.models import User
from my_voice.settings import MEDIA_URL, MEDIA_ROOT


class Article(models.Model):
    title = models.CharField(max_length=120)
    post_fin = models.FileField('Документ', upload_to='images/video')

    def get_absolute_file_upload_url(self):
        # return MEDIA_URL + self.post_fin.url
        # return MEDIA_ROOT + self.post_fin.url
        return self.post_fin.url

    def __str__(self):
        return self.title