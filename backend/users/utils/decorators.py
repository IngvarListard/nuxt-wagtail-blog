from functools import wraps
from django.core.exceptions import PermissionDenied
from django.utils.decorators import available_attrs
from django.utils import six
from graphql import ResolveInfo


def user_passes_test(test_func, msg='403::Отказано в доступе'):
    """
    Декоратор для резолверов GraphQL который проверяет проходит пользователь
    определенный тест или нет. Тест должен быть callable принимающим объект пользователя
    и возвращающий True если пользователь удовлетворяет условиям теста.
    """

    def decorator(resolver_func):
        @wraps(resolver_func, assigned=available_attrs(resolver_func))
        def _wrapped_view(*args, **kwargs):
            for arg in args:
                if isinstance(arg, ResolveInfo):
                    if test_func(arg.context.user):
                        return resolver_func(*args, **kwargs)
                    else:
                        raise PermissionDenied(msg)
        return _wrapped_view
    return decorator


def login_required(func=None, msg='401::Необходимо осуществить вход в систему'):
    """
    Декоратор для резолверов GraphQL который проверяет
    залогинен пользователь или нет
    """
    actual_decorator = user_passes_test(lambda u: u.is_authenticated, msg)
    if func:
        return actual_decorator(func)
    return actual_decorator


def permission_required(perm, msg='403::Недостаточно прав'):
    """
    Декоратор для резолверов GraphQL который проверяет
    наличие у пользователя того или иного разрешения
    """
    def check_perms(user):
        if isinstance(perm, six.string_types):
            perms = (perm, )
        else:
            perms = perm
        return user.has_perms(perms)

    return user_passes_test(check_perms, msg)

