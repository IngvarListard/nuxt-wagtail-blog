# Generated by Django 2.2.6 on 2019-10-06 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPage',
        ),
    ]
