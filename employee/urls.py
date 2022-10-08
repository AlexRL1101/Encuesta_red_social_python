from django.urls import path

from . import views

urlpatterns = [
    path('result/', views.employees_result, name='employees-result'),
    path('create/', views.employees_list, name='employees-list'),
    path('message/', views.employees_message, name='employees-message'),
    path('', views.nueva_encuesta, name='nueva_encuesta'),
    # path('edit/<str:pk>/', views.edit_employee, name='edit-employee'),
    # path('delete/<str:pk>/', views.delete_employee, name='delete-employee'),
]
