from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api
from django.urls import path
from knox import views as knox_views
from .api import RegisterAPI, LoginAPI

router = DefaultRouter()
router.register(r'posts', api.PostViewSet, basename="post")
router.register(r'comments', api.CommentViewSet, basename='comment')

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('', include(router.urls)),
]
