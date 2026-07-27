from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('check-username/', views.check_username, name='check_username'),
    path('mypage/', views.mypage, name='mypage'),

    path('profile_update/', views.profile_update, name='profile_update'),
    path('password_update/', views.password_update, name='password_update'),
    path('accounts_delete/', views.accounts_delete, name='accounts_delete')
]