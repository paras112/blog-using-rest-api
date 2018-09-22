from rest_framework .generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView,RetrieveUpdateAPIView
from posts.models import Post
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,

	)
from .serializers import PostListSerializer,PostDetailSerializer,PostCreateUpdateSerializer
class PostListAPIView(ListAPIView):
	queryset=Post.objects.all()
	serializer_class=PostListSerializer
class PostDetailAPIView(RetrieveAPIView):
	queryset=Post.objects.all()
	serializer_class=PostDetailSerializer
	lookup_field='slug'
class PostDeleteAPIView(DestroyAPIView):
	queryset=Post.objects.all()
	serializer_class=PostDetailSerializer
	lookup_field='slug'
class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset=Post.objects.all()
	serializer_class=PostDetailSerializer
	lookup_field='slug'
	permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
class PostCreateAPIView(CreateAPIView):
	queryset=Post.objects.all()
	serializer_class=PostCreateUpdateSerializer
	permission_classes=[IsAuthenticated]
	def perform_create(self,serializer):
		serializer.save(user=self.request.user)

	