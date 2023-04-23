from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from posts.models import Post, Group, Comment
from api.serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import AuthorDeleteOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthenticated, AuthorDeleteOnly)
    
    def perform_create(self, serializer):
        serializer.validated_data["author"] = self.request.user
        super().perform_create(serializer)
        


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthenticated)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthenticated, AuthorDeleteOnly)
