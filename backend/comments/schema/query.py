import graphene
from django.db.models import Count

from backend.comments.models import Comment
from backend.comments.schema.types import PagedCommentsNode


# noinspection PyMethodMayBeStatic
from backend.core.utils import id_generator


class Query(graphene.ObjectType):
    comments = graphene.Field(
        PagedCommentsNode,
        instance_id=graphene.ID(required=True, description='ID экземпляра с комментариями'),
        model_name=graphene.String(required=True, description='Имя модели в формате app_label.ModelName'),
        skip=graphene.Int(required=True, description='Пагинация, сколько объектов пропустить от начала'),
        first=graphene.Int(required=True, description='Пагинация. Количество объектов на странице'),
    )

    def resolve_comments(self, info, skip, first, **kwargs):
        app, model = kwargs['model_name'].split('.')
        instance_comments = (
            Comment.objects
                .filter(object_id=kwargs['instance_id'],
                        content_type__app_label=app,
                        content_type__model=model,
                        parent__isnull=True)
                .annotate(child_count=Count('children'))
            )
        total_count = instance_comments.count()
        paged_comments = instance_comments[:skip][first:]
        paged_comments_node = PagedCommentsNode(
            comments=paged_comments,
            total_count=total_count
        )
        id_ = id_generator(
            paged_comments_node,
            kwargs['model_name'],
            kwargs['instance_id']
        )
        paged_comments_node.id = id_
        return paged_comments_node
