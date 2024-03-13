from django.urls import path

from .views import file_contents
urlpatterns = [
    path('', file_contents, name='lessons')
]