from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ('__all__')
        read_only_fields = ('id', 'author', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('__all__')
        read_only_fields = ('id', )


class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('id', 'author', 'post', 'created')
