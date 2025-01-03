from django.urls import path
from .views import UserLoginView, PanelView, UserListView, UserCreateView, UserUpdateView

app_name = "app_login"

urlpatterns = [
    path('login/', UserLoginView.as_view() , name='login'),
    path('panel/', PanelView.as_view() , name='panel'),
    path('users/', UserListView.as_view() , name='user_list'),
    path('users/create/', UserCreateView.as_view() , name='user_create'),
    path('users/<int:pk>/edit', UserUpdateView.as_view() , name='user_edit'),
]