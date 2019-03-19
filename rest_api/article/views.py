from django.http import JsonResponse
from django.middleware import csrf
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions

from .models import Article
from .serializer import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request):
    return Response({
        'users': reverse('article:user-list'),
        'articles': reverse('article:article-list')
    })


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserArticleList(ArticleList):
    def get_queryset(self):
        owner = User.objects.get(username=self.kwargs['username'])
        return Article.objects.filter(owner=owner)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def get_csrf_token(request):
    csrftoken = csrf.get_token(request)
    return JsonResponse({'csrftoken': csrftoken})


