from abc import ABCMeta, abstractmethod
from typing import Type, Union

from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class Service(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        raise NotImplemented

    @staticmethod
    def resolve_field(
        value: Union[int, str, models.Model],
        model: Type[models.Model]
    ):
        if isinstance(value, models.Model):
            return value
        try:
            return model.objects.get(id=value)
        except model.DoesNotExist:
            raise ObjectDoesNotExist('Объекта за который вы хотите проголосовать не существует')
