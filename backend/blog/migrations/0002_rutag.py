# Generated by Django 2.2.6 on 2019-10-20 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuTag',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('taggit.tag',),
        ),
    ]
