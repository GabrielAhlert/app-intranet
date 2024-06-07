from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_recado/<int:id_recado>/', views.get_recado, name='get_recado'),
    path('get_eventos/<str:data>/', views.get_eventos, name='get_eventos'),
    path('get_days_with_events/<str:month_year>/', views.get_days_with_events, name='get_days_with_events'),
    path('get_eventos_mes/<str:month_year>/', views.get_eventos_mes, name='get_eventos_mes'),
]