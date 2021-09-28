from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_index, name='produtos'),
    path('formulario/', views.produtos_form, name='formulario'),
    path('salvar/', views.produtos_salvar, name='salvar'),
]
