from django.urls import path

from portfolio import views

urlpatterns = [
    path('portfolio/', views.rock,name='rock')
]

