from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='register-home'),
    path('saveregistration', views.saveregistration, name='register-save')
]
