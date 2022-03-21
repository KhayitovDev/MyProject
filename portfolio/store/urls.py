from django.urls import path
from . import views

urlpatterns = [

    path('homepage/', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('salad/', views.salad, name='salad'),
    path('noodle/', views.noodle, name='noodle'),
]
