from django.urls import path
from rest_framework.routers import SimpleRouter 

# from .views import PostDetail, PostList, UserDetail, UserList
from .views import UserviewSet, PostViewSet

router = SimpleRouter()

router.register('users', UserviewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls

# urlpatterns = [
#     path("users/", UserList.as_view()),
#     path("users/<int:pk>/", UserDetail.as_view()),
#     path("<int:pk>/", PostDetail.as_view()),
#     path("", PostList.as_view()),
# ]
