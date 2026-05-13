from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from .models import (
    UserProfile, Follow, Post, Content,
    PostLike, Comment, CommentLike,
    SavePost, SavePostItem, Storia
)
from .serializers import (
    UserProfileSerializer, UserProfileListSerializer, UserProfileDetailSerializer,
    FollowSerializer, PostListSerializer, PostDetailSerializer, ContentSerializer,
    PostLikeSerializer, CommentSerializer, CommentLikeSerializer,
    SavePostSerializer, SavePostItemSerializer, StoriaSerializer
)


class RegisterView(generics.CreateAPIView):
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            "user": serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'detail': 'Refresh токен не предоставлен.'}, status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Вы успешно вышли.'}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({'detail': 'Недействительный токен.'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer


class UserProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class FollowListAPIView(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class FollowCreateAPIView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class FollowDeleteAPIView(generics.DestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class ContentCreateAPIView(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class PostLikeListAPIView(generics.ListAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer


class PostLikeCreateAPIView(generics.CreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)


class CommentLikeCreateAPIView(generics.CreateAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer


class SavePostDetailAPIView(generics.RetrieveAPIView):
    queryset = SavePost.objects.all()
    serializer_class = SavePostSerializer

    def get_queryset(self):
        return SavePost.objects.filter(user=self.request.user)


class SavePostItemCreateAPIView(generics.CreateAPIView):
    queryset = SavePostItem.objects.all()
    serializer_class = SavePostItemSerializer


class SavePostItemDeleteAPIView(generics.DestroyAPIView):
    queryset = SavePostItem.objects.all()
    serializer_class = SavePostItemSerializer


class StoriaListAPIView(generics.ListAPIView):
    queryset = Storia.objects.all()
    serializer_class = StoriaSerializer


class StoriaCreateAPIView(generics.CreateAPIView):
    queryset = Storia.objects.all()
    serializer_class = StoriaSerializer


class StoriaDeleteAPIView(generics.DestroyAPIView):
    queryset = Storia.objects.all()
    serializer_class = StoriaSerializer

    def get_queryset(self):
        return Storia.objects.filter(user=self.request.user)