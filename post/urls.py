from django.urls import path
from .api import PostCreateApi, PostApi, PostUpdateApi, PostDeleteApi

urlpatterns = [
    path('api/create', PostCreateApi.as_view()),
    path('api/', PostApi.as_view()),
    path('api/<int:pk>', PostUpdateApi.as_view()),
    path('api/<int:pk>/delete', PostDeleteApi.as_view()),
]
