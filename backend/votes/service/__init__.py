from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property

from backend.blog.models import BlogPage
from backend.votes.models import Vote


class VoteArticle:
    """Лайк/дизлай статьи блога"""
    def __init__(self, user_id, article_id, action):
        self.user_id = user_id
        self.article_id = article_id
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
        user_vote = self.article.votes.filter(user_id=self.user_id)
        if user_vote and user_vote[0].vote == 1:
            user_vote.delete()
            return
        if user_vote and user_vote[0].vote == -1:
            user_vote.delete()
        return self.create_vote(Vote.LIKE)

    def dislike(self):
        user_vote = self.article.votes.filter(user_id=self.user_id)
        if user_vote and user_vote[0].vote == -1:
            user_vote.delete()
            return
        if user_vote and user_vote[0].vote == 1:
            user_vote.delete()
        return self.create_vote(Vote.DISLIKE)

    def create_vote(self, vote):
        content_type = ContentType(app_label='blog', model='BlogPage')
        content_object = content_type.get_object_for_this_type(id=self.article_id)
        return Vote.objects.create(vote=vote, content_object=content_object, user_id=self.user_id)

    @cached_property
    def article(self) -> BlogPage:
        return BlogPage.objects.get(id=self.article_id)

