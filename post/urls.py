from django.urls import path
from knox import views as knox_views
from .api import PostCreateApi, PostApi, PostUpdateApi, PostDeleteApi, RegisterAPI, LoginAPI

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/create', PostCreateApi.as_view()),
    path('api/', PostApi.as_view()),
    path('api/<int:pk>', PostUpdateApi.as_view()),
    path('api/<int:pk>/delete', PostDeleteApi.as_view()),
]
