from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
    path('', views.AppoinmentCreateView.as_view() , name='appoinment'),
    
    # path('', views.appoinment_form , name='appoinment'),

    path('appoinment/<pk>/', views.appoinment_render_pdf_view, name = "appoinment_pdf"),
]
