import re
import graphene
from promise import Promise, is_thenable, promise
from collections import OrderedDict

# Решает проблему переодического неотображения некоторых select'оров
promise.async_instance.disable_trampoline()


class Mutation(graphene.Mutation):
    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(cls, output=None, input_fields=None, arguments=None, name=None, **options):
        input_class = getattr(cls, 'Input', None)
        base_name = re.sub('Payload$', '', name or cls.__name__)

        assert not output, "Can't specify any output"
        assert not arguments, "Can't specify any arguments"

        bases = (graphene.InputObjectType,)
        if input_class:
            bases += (input_class,)

        if not input_fields:
            input_fields = {}

        cls.Input = type('{}Input'.format(base_name), bases, OrderedDict(input_fields))

        arguments = OrderedDict(input=cls.Input(required=True))
        resolve_mutate = getattr(cls, 'resolve_mutate', None)
        if cls.mutate and cls.mutate.__func__ == Mutation.mutate.__func__:
            assert resolve_mutate, (
                "{name}.resolve_mutate method is required"
                " in a Mutation.").format(name=name or cls.__name__)

        if not name:
            name = '{}Payload'.format(base_name)

        super().__init_subclass_with_meta__(
            output=None,
            arguments=arguments,
            name=name,
            **options
        )

    # noinspection PyShadowingBuiltins
    @classmethod
    def mutate(cls, root, info, input):
        def on_resolve(payload):
            return payload

        result = cls.resolve_mutate(root, info, **input)
        if is_thenable(result):
            return Promise.resolve(result).then(on_resolve)

        return on_resolve(result)

    @staticmethod
    def resolve_mutate(root, info, **kwargs):
        raise NotImplementedError
