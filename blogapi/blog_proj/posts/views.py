from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

class UserList(generics.ListCreateAPIView):
    # queryset = get_user_model().objects.all()
    users = get_user_model().objects.all()
    user_list = [user for user in users]
    print(user_list[0])
    # queryset = get_user_model()
    queryset = user_list

    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = get_user_model()
    # users = get_user_model().objects.all()
    # user_list = [user for user in users]
    queryset = get_user_model()
    serializer_class = UserSerializer



class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) 
    queryset = Post.objects.all()
    serializer_class = PostSerializer




class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)  #restrict access to views
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Custom perms
    permission_classes = (IsAuthorOrReadOnly,)
