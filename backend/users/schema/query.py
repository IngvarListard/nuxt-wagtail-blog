import graphene

from backend.users.utils.decorators import login_required
from backend.users.models import User
from backend.users.schema.types import BasicUserType


class Query(graphene.ObjectType):
    all_users = graphene.List(BasicUserType)
    get_current_user = graphene.Field(BasicUserType)

    # @login_required
    def resolve_all_users(self, info):
        from backend.notifications.tasks import test_task
        return User.objects.all()

    def resolve_get_current_user(self, info):
        user = info.context.user if info.context.user.is_authenticated else None
        return user
