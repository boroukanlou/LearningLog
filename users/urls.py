import django
from django.urls import include, path
from . import views

from . import views

app_name = 'users'

urlpatterns=[
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register')
]