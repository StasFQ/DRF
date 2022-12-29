from knox.models import AuthToken
from rest_framework import generics
from rest_framework.response import Response
from .serializer import PostSerializer, UserSerializer, RegisterSerializer
from .models import Post
from django.contrib.auth import login

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class PostCreateApi(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostApi(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteApi(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
