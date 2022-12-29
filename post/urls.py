from django.urls import path
from knox import views as knox_views
from .api import PostCreateApi, PostApi, PostUpdateApi, PostDeleteApi, RegisterAPI, LoginAPI, CommentCreateApi, \
    CommentUpdateApi, CommentDeleteApi, CommentApi

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/create/post', PostCreateApi.as_view()),
    path('api/post', PostApi.as_view()),
    path('api/<int:pk>/post', PostUpdateApi.as_view()),
    path('api/<int:pk>/delete/post', PostDeleteApi.as_view()),
    path('api/create/comment', CommentCreateApi.as_view()),
    path('api/comment', CommentApi.as_view()),
    path('api/<int:pk>/comment', CommentUpdateApi.as_view()),
    path('api/<int:pk>/delete/comment', CommentDeleteApi.as_view()),
]
