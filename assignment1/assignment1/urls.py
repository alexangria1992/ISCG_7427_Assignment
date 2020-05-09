
from django.contrib import admin
from django.urls import path
from amsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register-user'),
      path('child/profile/', views.child_profile, name='child-profile'),
    path('myprofile/', views.my_profile, name='my-profile'),
    path('calendar/', views.calendar, name='calendar'),
    path('logout/', views.logout_view, name='logout'),
    path('update/child/', views.updateChild, name = 'update-child'),
    path('register/', views.register_view, name='register-user'),
    path('remove/child/', views.remove_child, name = 'remove-child'),



]
