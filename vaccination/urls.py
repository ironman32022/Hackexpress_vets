from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.CustomerListView.as_view(), name = "customer-list-view"),
    path('test/', views.render_pdf_view, name = "test-view"),
    path('pdf/<pk>/', views.customer_render_pdf_view, name = "customer-pdf-view"),

]
