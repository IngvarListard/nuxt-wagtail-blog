import graphene
from graphene_django import DjangoObjectType

from backend.blog.models import BlogPage, Recipe
from backend.core.api.graphene_wagtail import DefaultStreamBlock, create_stream_field_type


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
    pass


class RecipeBlock(DefaultStreamBlock):
    recipe = graphene.Field(RecipeNode)

    def resolve_recipe(self, info):
        return Recipe.objects.get(id=self.value)


class BlogPageBody(graphene.Union):
    class Meta:
        types = (ParagraphBlock, HeadingBlock, RecipeBlock)


class ArticleNode(DjangoObjectType):
    (body, resolve_body) = create_stream_field_type(
        'body',
        paragraph=ParagraphBlock,
        heading=HeadingBlock,
        recipe=RecipeBlock,
        code=CodeBlock,
    )

    class Meta:
        model = BlogPage
        only_fields = ['id', 'title', 'date', 'intro']
