from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='list'),
    path('update_duty/<str:pk>/',views.updateDuty,name='update_duty'),
     path('delete_duty/<str:pk>/',views.deleteDuty,name='delete_duty'),
]