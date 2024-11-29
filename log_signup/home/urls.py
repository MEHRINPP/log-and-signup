from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.loginn,name='login'),
    path('success',views.success,name='success'),
    path('logout',views.custom_logout,name='logout'),
]
