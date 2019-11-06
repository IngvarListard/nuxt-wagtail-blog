import graphene


class PagedNode(graphene.ObjectType):
    class Meta:
        abstract = True

    has_next = graphene.Boolean()
    total_count = graphene.Boolean()
