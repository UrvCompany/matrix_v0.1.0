from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='home'),
    path('about', views.about, name='about'),
    path('rain', views.matrix_rain, name='rain')

]
