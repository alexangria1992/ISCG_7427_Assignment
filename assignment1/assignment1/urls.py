
from django.contrib import admin
from django.urls import path
from amsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register-user')

]
