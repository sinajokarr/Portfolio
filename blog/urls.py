from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProfileViewSet, CategoryViewSet, PostViewSet, MenuViewSet, DocumentViewSet, contact

router = DefaultRouter()
router.register(r"profile", ProfileViewSet, basename="profile")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"posts", PostViewSet, basename="post")
router.register(r"menu", MenuViewSet, basename="menu")
router.register(r"documents", DocumentViewSet, basename="document")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("contact/", contact, name="contact"),
]
