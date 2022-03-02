from django.urls import path

from . import views


urlpatterns = [
    path('',views.login),
    path('register', views.register, name='register' ),
    path('home', views.home, name='home' ),
    path('add', views.add, name='add'),
    # path('register',register),
    # path('display', views.display, name='display'),
    # path('logout', logout, name='logout'),
    # path('add_donor', views.add_donor, name='add_donor')
    
]