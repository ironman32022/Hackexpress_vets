from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('pet-symptom-checker', views.pet_checker, name='pet-symptom-checker'),
    path('meetup/', views.meetup, name='meetup'),
    path('ticket/<pk>/', views.meetup_render_pdf_view, name = "ticket"),
    path('medical/', views.medical, name = "medical"),
    
]
