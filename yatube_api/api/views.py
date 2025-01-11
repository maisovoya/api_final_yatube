from django.shortcuts import get_object_or_404
from rest_framework import pagination, permissions, viewsets, mixins
from rest_framework.filters import SearchFilter

from posts.models import Group, Post, User
from .permissions import OwnerOrReadOnly
from .serializers import (GroupSerializer,
                          PostSerializer, UserSerializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer