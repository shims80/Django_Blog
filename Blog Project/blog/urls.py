from django.urls import path
from . import views 
from . import views 

urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),
    path('register/', views.about,name='blog-register'),
]
