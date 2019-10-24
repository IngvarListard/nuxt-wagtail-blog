import graphene
import requests
import graphql_social_auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from graphene_file_upload.scalars import Upload
from social_django.utils import psa

from backend.users.schema.types import BasicUserType


# noinspection PyMethodMayBeStatic
class CreateUser(graphene.Mutation):
    test = graphene.String()

    class Arguments:
        a = graphene.String()

    def mutate(self, info, a):
        return a


# noinspection PyMethodMayBeStatic
class Login(graphene.Mutation):
    user = graphene.Field(BasicUserType)
    success = graphene.Boolean()

    class Meta:
        description = 'Вход пользователя в систему'

    class Arguments:
        login = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        print(kwargs)
        user = authenticate(info.context, **kwargs)
        if user is not None:
            login(info.context, user)
        return Login(user=user, success=user is not None)


# noinspection PyMethodMayBeStatic
class Logout(graphene.Mutation):
    class Meta:
        description = 'Выход пользователя из системы'

    success = graphene.Boolean(required=True, description='Успех операции')

    @staticmethod
    def mutate(root, info):
        if info.context.user.is_authenticated:
            logout(info.context)
            return Logout(success=True)
        else:
            return Logout(success=False)


class SocialAuth(graphene.Mutation):
    class Meta:
        description = 'Войти через социальные сети'

    class Arguments:
        code = graphene.String(required=True, description='Код активации')

    success = graphene.Boolean()

    def mutate(self, info, code, redirect_uri):
        psa()
        vk_uri = 'https://oauth.vk.com/access_token'
        params = {
            'client_id': '7178463',
            'client_secret': 'LYsil52OMOxwYXvo8CRX',
            'redirect_uri': redirect_uri,
            'code': code
        }
        r = requests.get(vk_uri, params=params)
User

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login = Login.Field()
    logout = Logout.Field()
    social_auth = graphql_social_auth.SocialAuth.Field()

