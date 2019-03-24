from django.contrib.auth import views as auth_views
from django.urls import include, path
from .views import my_logout, SingUpView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', my_logout, name='logout'),
    path('singup/', SingUpView.as_view(), name='singup'),
]