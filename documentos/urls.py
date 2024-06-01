from django.urls import path

from . import views

urlpatterns = [
    path('<int:Categorias_id>/', views.index, name='index'),

]