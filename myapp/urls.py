from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('principal/', views.principal,name='principal'),
    path('admission/', views.admission,name='admission'),
    path('gallery/', views.gallery,name='gallery'),
    path('contact/', views.contact,name='contact'),
    path('event/', views.event,name='event'),
    path('admission/', views.admission,name='admission'),
    path('mission-vission/', views.mission,name='mission-vission'),
    path('department/', views.department,name='department'),
    path('course/', views.course,name='course'),
    path('extra-curricular/', views.extra_curricular,name='extra_curricular'),
    path('study-material/', views.study_material,name='study-materials'),
]
