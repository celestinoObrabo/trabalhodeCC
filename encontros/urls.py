from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('<int:id>',views.home, name = 'home'),
    path('edit/<int:id>', views.editEncontro, name="EditE"),
    path('delete/<int:id>',views.deleteEncontro, name = 'deleteE'),
]