# Generated by Django 2.2.6 on 2019-10-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_recipe_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='views',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]
