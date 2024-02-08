from django.urls import path
from django1 import views
urlpatterns = [
    path('django2/', views.recap_view,name='rock')
]
