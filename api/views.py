from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from django.shortcuts import get_object_or_404

from posts.models import Post, Group
from api.serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import AuthorCreateorDeleteOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsAuthenticated, AuthorCreateorDeleteOnly)

    def perform_create(self, serializer):
        serializer.validated_data["author"] = self.request.user
        serializer.save()


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthenticated)

    def create(self, request, *args, **kwargs):
        # тут не совсем понял. Есть какой-то встроенный класс
        # или мне самому прописать?
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsAuthenticated, AuthorCreateorDeleteOnly)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.validated_data["author"] = self.request.user
        serializer.validated_data["post"] = get_object_or_404(
            Post, pk=self.kwargs.get('post_id'))
        serializer.save()
