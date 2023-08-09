from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView


menu = [
    {'title': 'about', 'url_name': 'about'},
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
        return Women.objects.filter(is_publish=True).select_related('cat')


def about(request):
    return render(request, 'women/about.html')


class register(CreateView):
    form_class = register_form
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class log_in(LoginView):
    form_class = login_form
    template_name = 'women/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

class log_out(View):
    def get(self, request):
        logout(request)
        return redirect('home')

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
    slug_url_kwarg = 'slug'
    context_object_name = 'post'


    def get_queryset(self):
        return Women.objects.only('title', 'content', 'photo', 'time_create', 'cat')


class contact(FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


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
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_publish=True).select_related('cat')


