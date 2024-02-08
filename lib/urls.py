from django.urls import path
from lib import views

urlpatterns=[
    path('bookupload/', views.book_upload,name='upload'),
    path('index/', views.index,name='index')
]