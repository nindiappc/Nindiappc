from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def visual(request):
    template = loader.get_template('nindia.html')
    return HttpResponse(template.render())

def nindia(request):
    template = loader.get_template('nindia.html')
    return HttpResponse(template.render())

def music(request):
    template = loader.get_template('music.html')
    return HttpResponse(template.render())

def product(request):
    template = loader.get_template('product.html')
    return HttpResponse(template.render())

def admin(request):
    template = loader.get_template('admin.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())