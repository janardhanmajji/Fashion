from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:item_pk>/', views.add_to_cart, name='add_to_cart'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',
         authentication_form=LoginForm), name='login'),
]
