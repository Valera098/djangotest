from django.urls import path, re_path

from coolsite import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('404/', login, name='pageNotFound'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>', show_post, name='post'),
    path('category/<int:cat_id>', show_category, name='category')

]