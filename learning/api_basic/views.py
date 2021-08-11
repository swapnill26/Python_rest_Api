from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# from rest_framework import status



# Function Base api.
@api_view(['GET','POST'])
def article_list(request):

    if request.method == 'GET':
        article=Article.objects.all()
        serializer=ArticleSerializer(article,many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer=ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)


@api_view(['GET','PUT','DELETE'])
def article_details(request,pk):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=200)

    if request.method=='GET':
        serializer=ArticleSerializer(article)
        return Response(serializer.data,status=201)

    elif request.method=='PUT':
        serializer=ArticleSerializer(article,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

    elif request.method=='DELETE':
        article.delete()
        return Response(status=200)

# Class Base api

class ArticleAPIViews(APIView):

    def get(self,request):
        article=Article.objects.all()
        serializer=ArticleSerializer(article,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)



    

