from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=160, blank=True)
    bio = models.TextField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    cv_file = models.FileField(upload_to="cv/", null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="posts")
    excerpt = models.CharField(max_length=220, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["slug", "created"])]

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    label = models.CharField(max_length=60)
    url = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.label


class Document(models.Model):
    file = models.FileField(upload_to="docs/")
    title = models.CharField(max_length=140, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or self.file.name
