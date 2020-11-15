from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView): # for read-write endpoint we use ListCreateAPIView
    # permission_classes = (permissions.IsAuthenticated,) # only login user can see this,here shows an HTTP 403 forbidden status code for a user who doesn't login
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView): # this view is using for CRUD operations(create,update,delete)
    # permission_classes = (permissions.IsAuthenticated,) # only authenticated user can check out this
    permission_classes = (IsAuthorOrReadOnly,) # this permission_classes define the author can update or delete,and other user just can read
    queryset = Post.objects.all()
    serializer_class = PostSerializer

