import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category__slug", lookup_expr="iexact")
    created_after = django_filters.IsoDateTimeFilter(field_name="created", lookup_expr="gte")
    created_before = django_filters.IsoDateTimeFilter(field_name="created", lookup_expr="lte")

    class Meta:
        model = Post
        fields = ["category", "created_after", "created_before"]
