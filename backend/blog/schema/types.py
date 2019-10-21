import graphene
from django.db.models import Count, When, Case, Q, Value
from graphene_django import DjangoObjectType

from backend.blog.models import BlogPage, Recipe, BlogPageTag
from backend.core.api.graphene_wagtail import DefaultStreamBlock, create_stream_field_type, WagtailImageNode
from wagtail.images.models import Image

from backend.votes.models import Vote
from backend.votes.schema.types import VoteNode


class IngredientBlock(DefaultStreamBlock):
    name = graphene.String()
    quantity = graphene.Float()
    unit = graphene.String()


class RecipeNode(DjangoObjectType):
    class Meta:
        model = Recipe

    ingredients, resolve_ingredients = create_stream_field_type(
        'ingredients',
        ingredient=IngredientBlock
    )

    instructions = graphene.List(graphene.String)

    def resolve_instructions(self, info):
        return [instruction.get('value') for instruction in self.instructions.stream_data]


class ParagraphBlock(DefaultStreamBlock):
    pass


class HeadingBlock(DefaultStreamBlock):
    pass


class CodeBlock(DefaultStreamBlock):
    language = graphene.String()
    code = graphene.String()


class ImageBlock(DefaultStreamBlock):
    image = graphene.Field(WagtailImageNode)

    def resolve_image(self, info):
        return Image.objects.get(id=self.value)


class MarkdownBlock(DefaultStreamBlock):
    pass


class RecipeBlock(DefaultStreamBlock):
    recipe = graphene.Field(RecipeNode)

    def resolve_recipe(self, info):
        return Recipe.objects.get(id=self.value)


class BlogPageBody(graphene.Union):
    class Meta:
        types = (ParagraphBlock, HeadingBlock, RecipeBlock)


class VotesCount(graphene.ObjectType):
    likes = graphene.Int(description='Количество лайков')
    dislikes = graphene.Int(description='Количество дизлайков')
    user_vote = graphene.String(description='Оценка пользователя')


# noinspection PyUnresolvedReferences
class ArticleNode(DjangoObjectType):
    (body, resolve_body) = create_stream_field_type(
        'body',
        paragraph=ParagraphBlock,
        heading=HeadingBlock,
        code=CodeBlock,
        markdown=MarkdownBlock,
        image=ImageBlock,
    )
    votes = graphene.List(VoteNode)
    votes_count = graphene.Field(VotesCount)

    def resolve_votes(self, info):
        return self.votes.all()

    def resolve_votes_count(self, info):
        votes_count = self.votes.aggregate(
            likes=Count('pk', filter=Q(vote=Vote.LIKE)),
            dislikes=Count('pk', filter=Q(vote=Vote.DISLIKE)),
        )
        vote = self.votes.filter(user_id=info.context.user.id)
        votes_count['user_vote'] = None
        if vote:
            votes_count['user_vote'] = 'like' if vote.vote == Vote.LIKE else 'dislike'

        return VotesCount(**votes_count)

    class Meta:
        model = BlogPage
        only_fields = ['id', 'title', 'date', 'intro', 'image', 'slug', 'head_image', 'tags', 'views', 'votes']

