from django.urls import include, path
from rest_framework import routers
from django.views.generic import TemplateView

from .views import (
                    PostViewSet, UserViewSet)

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'users', UserViewSet)


urlpatterns = [
    path('api/v1/', include(router_v1.urls)),
    path('api/v1/', include('djoser.urls.jwt')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]