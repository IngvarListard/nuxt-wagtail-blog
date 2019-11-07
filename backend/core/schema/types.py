import graphene

from backend.core.utils.decorators import classproperty


class PagedNode(graphene.ObjectType):
    class Meta:
        abstract = True

    has_next = graphene.Boolean()
    total_count = graphene.Boolean()

    # noinspection PyMethodParameters
    @classproperty
    def pagination_kwargs(cls):
        return {
            'page': graphene.Int(required=True, description='Номер страницы'),
            'per_page': graphene.Int(required=True, description='Количество элеменов на странице'),
        }
