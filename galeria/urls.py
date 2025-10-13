from django.urls import path
from galeria.views import index, index2, index3

urlpatterns = [
    path('', index),
    path('index2', index2),
    path('index3', index3),
]
