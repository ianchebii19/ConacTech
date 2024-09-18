from django.contrib import admin
from django.urls import path, include
from dashboard import views as dashboard_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include( 'dashboard.urls')),
    path('register/', dashboard_views.register, name='register'),
     path('login/', auth_views.LoginView.as_view(templatename ='dashboard/login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(templatename ='dashboard/logout.html'), name='logout')

]
