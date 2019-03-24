from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def my_logout(req):
    logout(req)
    return redirect('/polls/')

class SingUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/singup.html'