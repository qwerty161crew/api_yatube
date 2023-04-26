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
        # serializer.validated_data["author"] = self.request.user
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsAuthenticated, AuthorCreateorDeleteOnly)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=get_object_or_404(
            Post, pk=self.kwargs.get('post_id')))
