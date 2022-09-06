from django.urls import path
from user_account import views

#TEMPLATES URLs

app_name = 'user_account'

urlpatterns=[
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
]
