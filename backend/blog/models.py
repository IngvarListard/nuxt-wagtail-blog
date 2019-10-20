from django.db import models
from django.db.models import Model
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase, Tag
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.models import Image
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.users.models import UserProfile
from wagtailmarkdownblock.blocks import MarkdownBlock
from wagtailcodeblock.blocks import CodeBlock
from slugify import slugify


class RuTag(Tag):
    class Meta:
        proxy = True

    def slugify(self, tag, i=None):
        return slugify(self.name)[:128]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('blog.BlogPage', on_delete=models.CASCADE, related_name='tagged_items')

    @classmethod
    def tag_model(cls):
        return RuTag


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


# это здесь только для примера
@register_snippet
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    ingredients = StreamField([
        ('ingredient', blocks.StructBlock([
            ('name', blocks.CharBlock()),
            ('quantity', blocks.DecimalBlock()),
            ('unit', blocks.ChoiceBlock(choices=[
                ('none', '(no unit)'),
                ('g', 'Grams (g)'),
                ('ml', 'Millilitre (ml)'),
                ('tsp', 'Teaspoon (tsp.)'),
                ('tbsp', 'Tablespoon (tbsp.)'),
            ]))
        ]))
    ])
    instructions = StreamField([
        ('instruction', blocks.TextBlock()),
    ])

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('image'),
        StreamFieldPanel('ingredients'),
        StreamFieldPanel('instructions'),
    ]

    def __str__(self):
        return self.title


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    head_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        # ('recipe', SnippetChooserBlock(Recipe)),  # оставил для примера
        ('code', CodeBlock(label='code')),
        ('markdown', MarkdownBlock()),
        ('image', ImageChooserBlock()),
    ])

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        ImageChooserPanel('head_image'),
        StreamFieldPanel('body'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]

    def save(self, *args, **kwargs):
        if not self.id:
            if self.slug:
                self.slug = slugify(self.slug)
            else:
                self.slug = slugify(self.title)[:250]
        super().save(*args, **kwargs)


