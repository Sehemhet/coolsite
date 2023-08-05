from django.urls import path
from .views import *

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('about/', about, name="about"),
    path('login/', login, name="login"),
    path('contact/', contact, name="contact"),
    path('add_post/', add_post.as_view(), name="add_post"),
    path('post/<slug:post_slug>', post.as_view(), name='post'),
    path('category/<slug:cat_slug>', category.as_view(), name='category'),
]