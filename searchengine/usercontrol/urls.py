from django.urls import path
from . import views

app_name = 'usercontrol'

urlpatterns = [
    path('login', views.LoginView),
    path('loginaction', views.LoginAction),
    path('logout', views.Logout),
    path('newpassword', views.NewPassword),
    path('newpassaction', views.NewPassAction),
    path('password', views.Password),
    path('questions', views.Questions)
]