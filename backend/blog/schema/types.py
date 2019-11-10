import graphene
from graphene_django import DjangoObjectType
from wagtail.images.models import Image

from backend.blog.models import BlogPage, Recipe
from backend.blog.service import CountVotes
from backend.comments.schema.types import CommentNode
from backend.core.api.graphene_wagtail import DefaultStreamBlock, create_stream_field_type, WagtailImageNode
from backend.core.schema.types import PagedNode
from backend.votes.schema.types import VoteNode, VotesCountNode


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
    votes_count = graphene.Field(VotesCountNode)

    def resolve_votes(self, info):
        return self.votes.all()

    # noinspection PyTypeChecker
    def resolve_votes_count(self, info):
        votes_counter = CountVotes(
            info.context.user.id,
            f'{self._meta.app_label}.{self._meta.model_name}',
            self.id
        )
        votes_count = votes_counter.execute()
        return VotesCountNode(
            id=f'__{self._meta.app_label}.{self._meta.model_name}_{self.id}',
            **votes_count
        )

    class Meta:
        model = BlogPage
        only_fields = ['id', 'title', 'date', 'intro', 'image', 'slug', 'head_image', 'tags', 'views', 'votes',
                       'comments', 'owner']


class PagedArticlesNode(PagedNode):
    articles = graphene.List(ArticleNode)
