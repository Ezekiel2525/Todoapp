from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('add/', views.add_forms, name = 'add'),
    path('complete/<int:todo_id>', views.complete, name = 'complete'),
    path('delete_complete/', views.delete_complete, name = 'delete_complete'),
    path('deleteall/', views.deleteall, name = 'deleteall'),
]
