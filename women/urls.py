from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(100)(home.as_view()), name="home"),
    path('about/', about, name="about"),
    path('login/', log_in.as_view(), name="login"),
    path('logout/', log_out.as_view(), name="logout"),
    path('register/', register.as_view(), name="register"),
    path('contact/', contact.as_view(), name="contact"),
    path('add_post/', add_post.as_view(), name="add_post"),
    path('post/<slug:slug>', post.as_view(), name='post'),
    path('category/<slug:cat_slug>', cache_page(300)(category.as_view()), name='category'),
]