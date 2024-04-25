from . import views
from django.urls import path, include
from .views import user_login

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', user_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls'))
]
