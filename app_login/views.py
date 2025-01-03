from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'app_login/login.html'


class PanelView(LoginRequiredMixin, TemplateView):
    template_name = 'app_login/panel.html'

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "app_login/user_list.html"
    context_object_name = "users"

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "app_login/user_create.html"
    success_url = reverse_lazy('app_login:user_list')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'app_login/user_edit.html'
    success_url = reverse_lazy('app_login:user_list')