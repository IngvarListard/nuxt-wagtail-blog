# Generated by Django 2.2.6 on 2019-10-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20191029_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
    ]