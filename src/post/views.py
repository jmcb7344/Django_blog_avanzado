from locale import format_string
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from post import forms, models
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PostList(generic.ListView):
    model = models.Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_pg'] = 'Lista de Post'
        return context

class PostDetail(generic.DetailView):
    model = models.Post

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            models.Vistas.objects.get_or_create(usuario=self.request.user, post=object)
        return object

    def post(self, *args, **kwargs):
        form = forms.CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            coment = form.instance
            coment.usuario = self.request.user
            coment.post = post
            form.save()
            return redirect('post:detail', slug=post.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.CommentForm()
        context['button'] = 'Comentar'
        return context

class CreatePost(generic.CreateView):
    model = models.Post
    form_class = forms.CreateForm
    success_url = reverse_lazy('post:home')

    """
    def get_success_url(self):
        return reverse('post:home')
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = 'Crear'
        return context

class UpdatePost(generic.UpdateView):
    model = models.Post
    form_class = forms.CreateForm
    success_url = reverse_lazy('post:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = 'Editar'
        return context

class DeletePost(generic.DeleteView):
    model = models.Post
    success_url = reverse_lazy('post:home')

class NuevoUser(generic.CreateView):
    model = User
    template_name = 'registro.html'
    form_class = forms.RegistroForm
    success_url = reverse_lazy('login')
    
class LikeView(generic.View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(models.Post, slug=slug)
        like_qs = models.Like.objects.filter(usuario=self.request.user, post=post)
        if like_qs.exists():
            like_qs[0].delete()
            return redirect('post:detail', slug)
        else:
            models.Like.objects.create(usuario=self.request.user, post=post)
            return redirect('post:detail', slug)

class sobre_mi(generic.TemplateView):
    """Vista sobre_mi"""
    template_name = 'post/sobremi.html'
        