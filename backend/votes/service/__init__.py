from typing import Union

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property

from django.apps import apps
from backend.blog.models import BlogPage
from backend.core.service import Service
from backend.votes.models import Vote


class ToVote(Service):
    """Лайк/дизлай статьи блога"""
    def __init__(
        self,
        user_id: int,
        instance: Union[int, str, models.Model],
        action: str,
        model_name: str
    ):
        """
        :param user_id: user_id
        :param instance: экземпляр объекта или его id, к которому нужно добавить голос
        :param action: тип голоса. Может быть "like", "dislike"
        :param model_name: имя модели через точку: app.Model
        """
        self.user_id = user_id
        self.instance = self.resolve_field(instance, apps.get_model(model_name))
        self.action = action

    def execute(self) -> Vote:
        if self.action == 'like':
            vote = self.like()
        elif self.action == 'dislike':
            vote = self.dislike()
        else:
            raise ValueError(f'Неизвестный тип действия "{self.action}"')
        return vote

    def like(self):
        user_vote = self.instance.votes.filter(user_id=self.user_id)
        if user_vote and user_vote[0].vote == 1:
            user_vote.delete()
            return
        if user_vote and user_vote[0].vote == -1:
            user_vote.delete()
        return self.create_vote(Vote.LIKE)

    def dislike(self):
        user_vote = self.instance.votes.filter(user_id=self.user_id)
        if user_vote and user_vote[0].vote == -1:
            user_vote.delete()
            return
        if user_vote and user_vote[0].vote == 1:
            user_vote.delete()
        return self.create_vote(Vote.DISLIKE)

    def create_vote(self, vote):
        content_type = ContentType(app_label='blog', model='BlogPage')
        content_object = content_type.get_object_for_this_type(id=self.instance.id)
        return Vote.objects.create(vote=vote, content_object=content_object, user_id=self.user_id)

