from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup_login/', views.signup_login, name='signup_login'),
    path('signup/', views.signup, name='signup'), 
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout') 
]