# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from .models import Articles
from .serializers import ArticlesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins


# GenericApi based ApiViews

class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()
    lookup_field = 'sno'

    def get(self, request, sno=None):
        if sno:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, sno=None):
        return self.update(request, sno)

    def delete(self, request, sno):
        return self.destroy(request, sno)


# Class based ApiViews

class ArticleApiView(APIView):

    @staticmethod
    def get(request):
        articles = Articles.objects.all()
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    @staticmethod
    def get_object(sno):
        try:
            return Articles.objects.get(sno=sno)

        except Articles.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, sno):
        article = self.get_object(sno)
        serializer = ArticlesSerializer(article)
        return Response(serializer.data)

    def put(self, request, sno):
        article = self.get_object(sno)
        serializer = ArticlesSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, sno):
        article = self.get_object(sno)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Function based ApiViews

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Articles.objects.all()
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, sno):
    try:
        article = Articles.objects.get(sno=sno)

    except Articles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticlesSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticlesSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
