from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'base/index.html', {})

def toc(request):
    return render(request, 'base/terms-conditions.html', {})

def faqs(request):
    return render(request, 'base/faqs.html', {})

def privacypolicy(request):
    return render(request, 'base/privacy-policy.html', {})
