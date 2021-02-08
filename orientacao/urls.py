from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="login"), name='logout'),
    path('register/', views.register, name='register'),
    path('orientacao/', views.index, name='index'),
    path('orientacao/<int:id>/', views.details, name='details'),
    path('orientacao/newOrient/', views.OrientacaoCreateView.as_view(), name='nova-orientacao'),
    path('orientacao/edit/<int:pk>', views.OrientacaoUpdateView.as_view(), name='editar-orientacao'),
    path('orientacao/delete/<int:id>', views.deleteOrient, name='deletar-orientacao'),
]
