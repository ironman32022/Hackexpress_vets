from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', views.login_page, name='Login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name='Logout'),
    path('accounts/register/', views.register_page, name='Register'),
    path('accounts/password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('accounts/password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('accounts/reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
