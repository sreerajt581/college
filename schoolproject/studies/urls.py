from django.urls import path
from . import views
app_name='studies'
urlpatterns = [

    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('newpage',views.newpage,name='newpage'),
    path('department',views.department,name='department'),
    path('home',views.home,name='home'),
]