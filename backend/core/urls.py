"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from backend.core.api import CustomGraphQLView
from .views import graphiql

admin.site.site_header = 'Администрирование'


def _csrf_exempt(view_func):
    """
    Функция оборачивает GraphQL API в вызов csrf_exempt,
    который позволяет избавиться от ошибок при запросах с другого хоста (в режиме разработки).
    На продакшене функция возвращает необернутый view_func, чтобы обеспечить защиту от CSRF.
    CSRF - https://en.wikipedia.org/wiki/Cross-site_request_forgery
    """
    if settings.DEBUG:
        return csrf_exempt(view_func)
    else:
        return view_func


urlpatterns = [
    path('api_v1', _csrf_exempt(CustomGraphQLView.as_view(
        graphiql=not settings.GRAPHQL_BATCH,
        batch=settings.GRAPHQL_BATCH,
    ))),
    path('admin/', admin.site.urls),
    path("ws/api_v1/", graphiql)
] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
