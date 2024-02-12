from django.urls import path
from . import views
from .views import map_view
from .views import home

urlpatterns = [
    path('inde/', views.profile, name='port'),
    path('profile/', views.profile, name='profile'),
    path('new/', views.new, name='new'),
    path('map/', map_view, name='map'),
    path('home/',views.home, name='home'),

]
