from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Posts, Category, LikeDislike, Comments, Statistics


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения юзера"""
    class Meta:
        model = User
        fields = ['username', 'password']


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для CRUD категории"""
    class Meta:
        model = Category
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения постов"""
    category = CategorySerializer()
    author = UserSerializer()

    class Meta:
        model = Posts
        exclude = ['published']


class CreatePostsSerializer(serializers.ModelSerializer):
    """Сериализатор для CRUD постов"""
    class Meta:
        model = Posts
        fields = '__all__'


class LikeDislikeSerializer(serializers.ModelSerializer):
    """Сериализатор для отображеня лайков и дизлайков"""

    class Meta:
        model = LikeDislike
        fields = ('like_or_dislike', )


class RecursiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'

        def recursive(self, value):
            serializer = self.parent.parent.__class__(value, context=self.context)
            return serializer.data


class CommentsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения комментов"""
    author_comment = UserSerializer()
    post = PostsSerializer()
    parent = RecursiveSerializer()

    class Meta:
        model = Comments
        fields = '__all__'


class CreateCommentsSerializer(serializers.ModelSerializer):
    """Сериализатор для CRUD комментов"""
    class Meta:
        model = Comments
        fields = '__all__'


class StatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistics
        fields = ('calculate_stat', )


