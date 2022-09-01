from urllib import request
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug':self.slug})

    def get_like_url(self):
        return reverse('post:like', kwargs={'slug':self.slug})

    @property
    def comment(self):
        return self.coment_set.all()

    @property
    def get_like_count(self):
        return self.like_set.all().count()

    @property
    def get_view_count(self):
        return self.vistas_set.all().count()

    @property
    def get_comment_count(self):
        return self.coment_set.all().count()

class Coment(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    coment = models.TextField()

    def __str__(self):
        return self.usuario.username

class Like(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username

class Vistas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username
