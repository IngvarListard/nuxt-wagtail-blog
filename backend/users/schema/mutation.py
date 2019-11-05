import graphene
import graphql_social_auth
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from graphene_file_upload.scalars import Upload

from backend.users.models import User
from backend.users.schema.types import BasicUserType


# noinspection PyMethodMayBeStatic
from backend.users.tasks import send_user_password


class Login(graphene.Mutation):
    user = graphene.Field(BasicUserType)
    success = graphene.Boolean()

    class Meta:
        description = 'Вход пользователя в систему'

    class Arguments:
        login = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
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


# noinspection PyMethodMayBeStatic
class UpdateAvatar(graphene.Mutation):
    user = graphene.Field(BasicUserType)

    class Arguments:
        user_id = graphene.ID(required=True)
        file = graphene.Argument(Upload, required=True)

    def mutate(self, info, user_id, file):
        assert file, 'Необходимо приложить файл'
        user = info.context.user
        if not user.is_superuser and int(user_id) != user.id:
            raise PermissionDenied('Нет прав на редактирование чужого аватара')
        user = User.objects.get(id=user_id)
        user.avatar.delete()
        user.avatar = file
        user.save()
        return UpdateAvatar(user=user)


# noinspection PyMethodMayBeStatic
class UpdateUserEmail(graphene.Mutation):
    user = graphene.Field(BasicUserType)

    class Arguments:
        id = graphene.ID(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        current_user = info.context.user
        user_id = kwargs.pop('id')
        if not current_user.is_superuser and int(user_id) != current_user.id:
            raise PermissionDenied('Нет прав на редактирование чужого email\'a')
        # TODO вставить арссылку писем с подтверждением для смены почты
        user = User.objects.get(id=user_id)
        user.email = kwargs.pop('email')
        user.save()
        return UpdateUserEmail(user=user)


class UpdateUserInfo(graphene.Mutation):
    user = graphene.Field(BasicUserType)

    class Arguments:
        id = graphene.ID(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        bio = graphene.String()
        display_name = graphene.String()

    def mutate(self, info, **kwargs):
        current_user = info.context.user
        user_id = kwargs.pop('id')
        if not current_user.is_superuser and int(user_id) != current_user.id:
            raise PermissionDenied('Нет прав на редактирование чужого аватара')
        user = User.objects.get(id=user_id)
        for attr, value in kwargs.items():
            setattr(user, attr, value)
        user.save()
        return UpdateUserInfo(user=user)


class UpdateUserPassword(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        # TODO подтверждение о смене пароля на почту
        current_user = info.context.user
        user_id = kwargs.pop('id')
        if not current_user.is_superuser and int(user_id) != current_user.id:
            raise PermissionDenied('Нет прав на редактирование чужого пароля')
        user = User.objects.get(id=user_id)
        user.set_password(kwargs.pop('password'))
        user.save()
        return UpdateUserPassword(success=True)


class SocialAuth(graphql_social_auth.SocialAuthMutation):
    user = graphene.Field(BasicUserType)

    class Arguments:
        provider = graphene.String(required=True)
        access_token = graphene.String(required=True)
        email = graphene.String()

    @classmethod
    def resolve(cls, root, info, social, **kwargs):
        if not social.user.email:
            social.user.email = kwargs.pop('email', None)
            social.user.save()
        if social.user.email and social.user.RAW_PASSWORD:
            send_user_password(social.user.email, social.user.RAW_PASSWORD).delay()
        return cls(user=social.user)


class Mutation(graphene.ObjectType):
    login = Login.Field()
    logout = Logout.Field()
    social_auth = SocialAuth.Field()
    update_avatar = UpdateAvatar.Field()
    update_user_info = UpdateUserInfo.Field()
    update_user_email = UpdateUserEmail.Field()

