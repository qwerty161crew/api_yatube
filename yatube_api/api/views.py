from django.shortcuts import render,  get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import viewsets

from posts.models import Post, Group, Comment
from api.serializers import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    # @action(methods=['get'], detail=True)
    def get(request, pk):
        if request.user.is_authenticated():
            post = get_object_or_404(Post, id=pk)
            serializer = PostSerializer(post, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    # @action(methods=['post'], detail=True)
    def create(request):
        if request.user.is_authenticated():
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


    # @action(methods=['update'], detail=True)
    def update(request, pk):
        post = get_object_or_404(Post, id=pk)
        if request.user == post.author and request.user.is_authenticated():
            serializer = PostSerializer(post, many=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # @action(methods=['list'], detail=True)
    def list(request):
        if request.user.is_authenticated():
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    # @action(methods=['delete'], detail=True)
    def delete(request, pk):
        post = get_object_or_404(Post, id=pk)
        if request.user == post.author:
            serializer = PostSerializer(post, many=False)
            post.delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)


class GroupViewSet(viewsets.ModelViewSet):
    
    # @action(methods=['get'], detail=True)
    def get(request, pk):
        if request.user.is_authenticated():
            group = get_object_or_404(Group, id=pk)
            serializer = GroupSerializer(group, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    # @action(methods=['list'], detail=True)
    def list(request):
        if request.user.is_authenticated():
            groups = Group.objects.all()
            serializer = GroupSerializer(groups, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class CommentViewSet(viewsets.ModelViewSet):
    # @action(methods=['get'], detail=True)
    def get(request, pk):
        if request.user.is_authenticated():
            comment = get_object_or_404(Comment, id=pk)
            serializer = CommentSerializer(comment, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    # @action(methods=['list'], detail=True)
    def list(request):
        if request.user.is_authenticated():
            comments = Comment.objects.all()
            serializer = GroupSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    # @action(methods=['post'], detail=True)
    def create(request):
        if request.user.is_authenticated():
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)






