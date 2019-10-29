import os
import ast
import graphene
from functools import singledispatch
from typing import Type


def get_bool_from_env(name, default_value):
    if name in os.environ:
        value = os.environ[name]
        try:
            return ast.literal_eval(value)
        except ValueError as e:
            raise ValueError('{} is an invalid value for {}'.format(value, name)) from e
    return default_value


@singledispatch
def id_generator(instance: graphene.ObjectType, parent_model_name, parent_model_id):
    if not getattr(instance, 'id', None):
        raise ValueError(
            f'Неизвестный тип "{type(instance)}". '
            f'Нельзя сгенерировать ID'
        )

