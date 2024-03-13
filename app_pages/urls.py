from django.urls import path

from app_pupils.models import pupils
from .views import index, about, contact, themes

urlpatterns = [
    path('', index, name='index_url'),
    path('about/', about, name='about_url'),
    path('contact/', contact, name='contact_url'),
    path('lessons/', themes, name='lessons'),
    path('pupils/', pupils, name='pupils')
]