# Generated by Django 4.1.4 on 2023-02-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
