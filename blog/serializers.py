from rest_framework import serializers
from .models import Profile,Category,Post,MenuItem,Document



class ProfileSerializer(serializers.ModelSerializer):
    class Meta :
        model = Profile
        fields = "__all__"
        
        
class CategorySerrilizers(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ["id", "name", "slug"]
        
        
class PostSerilizers(serializers.ModelSerializer):
    class Meta :
        model = Post
        fields = ["id", "title", "slug", "excerpt", "category", "created"]


class MenuItemSerializers(serializers.ModelSerializer):
    class Meta :
        model = MenuItem
        fields = "__all__"
        

class MenuItemSerilizers(serializers.ModelSerializer):
    class Meta :
        model =MenuItem
        fields = ["label", "url", "order"]
        
        
class DocumentSerilizers(serializers.ModelSerializer):
    class Meta :
        model = Document
        fields = ["id", "title", "file", "uploaded_at"]
        