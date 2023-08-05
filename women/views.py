from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


menu = [
    {'title': 'about', 'url_name': 'about'},
    {'title': 'login', 'url_name': 'login'},
    {'title': 'add_post', 'url_name': 'add_post'},
    {'title': 'contact', 'url_name': 'contact'}
]
class home(ListView):
    paginate_by = 3
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'главная страница'
        context['cats'] = Category.objects.annotate(Count('women'))
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_publish=True)


def about(request):
    return render(request, 'women/about.html')

def login(request):
    return HttpResponse('<h1>login</h1>')

class add_post(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/add_post.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

class post(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cats'] = Category.objects.annotate(Count('women'))
        context['cat_selected'] = 1
        return context

def contact(request):
    return HttpResponse(request, '<h1>add_post</h1>')

class category(ListView):
    paginate_by = 3
    model = Women, Category
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'главная страница'
        context['cats'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_publish=True)