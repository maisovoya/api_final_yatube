from django.urls import include, path
from rest_framework import routers

from .views import (PostViewSet, GroupViewSet,
                    CommentViewSet, FollowViewSet)


router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"groups", GroupViewSet, basename="groups")
router.register(r"follow", FollowViewSet, basename="follows")
router.register(
    r"posts/(?P<post_id>[^/.]+)/comments", CommentViewSet, basename="comments"
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
