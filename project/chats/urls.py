from django.urls import path
from chats import views

urlpatterns=[
    path('',views.index,name='index'),
]