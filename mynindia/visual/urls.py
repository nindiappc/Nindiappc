from django.urls import path
from . import views

urlpatterns = [
    path('visual', views.visual, name='visual'),
    path('nindia', views.nindia, name='nindia'),
    path('profile', views.profile, name='profile'),
    path('music', views.music, name='music'),
    path('product', views.product, name='product'),
    path('admin', views.admin, name='admin'),
    path('about', views.about, name='about'),
]