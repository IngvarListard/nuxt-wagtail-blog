# Generated by Django 2.2.6 on 2019-10-28 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='changed',
            field=models.BooleanField(default=False, verbose_name='Изменено'),
        ),
    ]