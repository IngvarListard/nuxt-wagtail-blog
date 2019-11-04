import os
import graphene
import graphene_django

from django.conf import settings
from backend.users.models import User


class UserType(graphene.Interface):

    class Meta:
        description = 'Абстрактный интерфейс пользователя'

    id = graphene.Int(required=True)
    first_name = graphene.String()
    last_name = graphene.String()
    login = graphene.String()
    email = graphene.String()
    is_active = graphene.String()
    is_superuser = graphene.String()
    display_name = graphene.String()
    avatar = graphene.String()
    bio = graphene.String()

    def resolve_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return os.path.join(settings.STATIC_URL, 'man.jpg')


class BasicUserType(graphene_django.DjangoObjectType):

    class Meta:
        model = User
        interface = (UserType,)
        description = 'Объект пользователя с базовой информацией'
        only_fields = ('id', 'first_name', 'last_name', 'is_active', 'is_superuser', 'email', 'display_name', 'avatar', 'bio')
