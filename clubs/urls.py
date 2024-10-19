from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('club/<int:pk>/',views.club,name='club'),
    path('createclub/',views.createclub,name='createclub')
]

