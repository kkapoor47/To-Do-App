from django.urls import path
from .views import home,editTask,deleteTask

urlpatterns = [
    path('',home, name='home'),
    path('edit_task/<str:pk>/',editTask,name='edit_task'),
    path('delete_task/<str:pk>/',deleteTask,name='delete_task'),


]
