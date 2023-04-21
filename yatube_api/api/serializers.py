from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        read_only_fields = ('id', 'author', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        field = ('id', 'title', 'slug', 'description')
        read_only_fields = ('id', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        field = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('id', 'author', 'post', 'created')




