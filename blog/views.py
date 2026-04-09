import logging
from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter
from .models import Profile, Category, Post, MenuItem, Document
from .serializers import (
    ProfileSerializer, CategorySerializer,
    PostListSerializer, PostDetailSerializer,
    MenuItemSerializer, DocumentSerializer
)

logger = logging.getLogger(__name__)

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
    name = request.data.get("name")
    email = request.data.get("email")
    message = request.data.get("message")

    if not all([name, email, message]):
        return Response(
            {"error": "All fields are required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        sender_email = getattr(settings, 'EMAIL_HOST_USER', 'noreply@example.com')
        recipient_email = getattr(settings, 'CONTACT_EMAIL', sender_email)

        print("\n" + "="*50)
        print("[DEBUG] INITIATING EMAIL SEQUENCE")
        print(f"[DEBUG] SENDER (From .env): {sender_email}")
        print(f"[DEBUG] RECIPIENT (From .env): {recipient_email}")
        print("="*50 + "\n")

        send_mail(
            subject=f"New Portfolio Inquiry: {name}",
            message=f"Sender: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=sender_email,
            recipient_list=[recipient_email],
            fail_silently=False,
        )
        
        print("[DEBUG] SUCCESS: Email pushed to Google SMTP servers.\n")
        
        return Response({"ok": True}, status=status.HTTP_200_OK)

    except Exception as e:
        print(f"\n[DEBUG] CRITICAL SMTP ERROR: {str(e)}\n")
        logger.error(f"SMTP Error: {str(e)}")
        return Response(
            {"error": "Server encountered an issue sending the email."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )