from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('terms-conditions', views.toc, name='toc'),
]