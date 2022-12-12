from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('terms-conditions', views.toc, name='toc'),
    path('FAQ', views.faqs, name='faqs'),
    path('privacy-policy', views.privacypolicy, name='privacypolicy'),
]