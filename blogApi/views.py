from django.shortcuts import render
from .models import BlogPost
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from blogApi.serializers import BlogPostSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

# class BlogView(APIView):

#     def get(self, request, *args, **kwargs):
#         posts = BlogPost.objects.all()
#         serializer = BlogPostSerializer(posts, many=True)

#         return Response(serializer.data)

@api_view(['GET', 'POST'])
def post_list(request, *args, **kwargs):

    if request.method == 'GET':
        posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(posts, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BlogPostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, *args, **kwargs):
    try:
        pk = int(kwargs['pk'])
        post = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogPostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BlogPostSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
