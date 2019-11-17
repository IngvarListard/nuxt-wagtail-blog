from django.db import models
from django.db.models import F


class EventQuerySet(models.QuerySet):
    def annotate_distance_to_point(self, x, y):
        return self.annotate(distance=((F('x')-x)*(F('x')-x)+(F('y')-y)*(F('y')-y))**(0.5))


class Event(models.Model):
    x = models.DecimalField(max_digits=9, decimal_places=6)
    y = models.DecimalField(max_digits=9, decimal_places=6)
    region_id = models.IntegerField()
    address = models.TextField('Адрес')
    description = models.TextField('Описание')
    name = models.TextField('Имя')
    slug = models.TextField()
    image_url = models.TextField('Изображение')
    date = models.DateField('Дата')

    objects = EventQuerySet.as_manager()