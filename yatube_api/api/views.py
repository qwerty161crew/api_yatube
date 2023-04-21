from django.shortcuts import render,  get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets

from posts.models import Post, Group, Comment
from api.serializers import PostSerializer, GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(request):
        if request.user.is_authenticated():
            post = Post.objects.all()
            serializer = PostSerializer(post, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def create(request):
        if request.user.is_authenticated():
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.author and request.user.is_authenticated():
            serializer = PostSerializer(post, many=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.author:
            serializer = PostSerializer(post, many=False)
            post.delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Comment.objects.all()
