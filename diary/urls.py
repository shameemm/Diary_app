from django.urls import path

from . import views


urlpatterns = [
    path('',views.login),
    path('register', views.register, name='register' ),
    # path('register',register),
    # path('display', views.display, name='display'),
    # path('logout', logout, name='logout'),
    # path('add_donor', views.add_donor, name='add_donor')
    
]