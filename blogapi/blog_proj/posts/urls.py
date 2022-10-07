from django.urls import path

from .views import PostDetail, PostList, UserDetail, UserList

urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
    path("<int:pk>/", PostDetail.as_view()),
    path("", PostList.as_view()),
]