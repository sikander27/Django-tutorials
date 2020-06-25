from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from pease import views

urlpatterns = [
    path('test',views.test, name='test'),
    path('emp',views.emp, name='emp'),
    path('show',views.show, name='show'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.destroy, name='delete'),
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='employee/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='employee/logout.html'), name='logout'),
    path('profile',views.profile,name='profile')
]