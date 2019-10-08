from wagtail.core.fields import StreamField
from graphene.types import Scalar

from graphene_django.converter import convert_django_field


class GenericStreamFieldType(Scalar):
    @staticmethod
    def serialize(stream_value):
        return stream_value.stream_data


def register_custom_serializers():
    @convert_django_field.register(StreamField)
    def convert_stream_field(field, registry=None):
        return GenericStreamFieldType(
            description=field.help_text, required=not field.null
        )
