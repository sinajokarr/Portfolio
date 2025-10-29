from rest_framework import viewsets, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend

from .filters import PostFilter
from .models import Profile, Category, Post, MenuItem, Document
from .serializers import (
    ProfileSerializer, CategorySerializer,
    PostListSerializer, PostDetailSerializer,
    MenuItemSerializer, DocumentSerializer
)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ["get", "put", "patch", "post"]
    def get_permissions(self):
        return [AllowAny()] if self.action in ["list", "retrieve"] else [IsAdminUser()]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PostFilter
    search_fields = ["title", "body", "excerpt", "category__name"]
    ordering_fields = ["created", "title"]
    ordering = ["-created"]
    def get_serializer_class(self):
        return PostDetailSerializer if self.action == "retrieve" else PostListSerializer

class MenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    def get_permissions(self):
        return [AllowAny()] if self.action in ["list", "retrieve"] else [IsAdminUser()]

@api_view(["POST"])
@permission_classes([AllowAny])
def contact(request):
    name = request.data.get("name", "-")
    email = request.data.get("email", "-")
    message = request.data.get("message", "-")
    send_mail(
        subject=f"Contact from {name}",
        message=f"Email: {email}\n\n{message}",
        from_email=None,
        recipient_list=["you@example.com"],
    )
    return Response({"ok": True})
