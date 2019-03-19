from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author', 'owner')


class UserSerializer(serializers.ModelSerializer):
    article_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'article_set')


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     article_set = serializers.HyperlinkedRelatedField(many=True, view_name='article:article-detail', read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'article_set',)
