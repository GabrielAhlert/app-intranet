from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_days_with_events/<str:month_year>/', views.get_days_with_events, name='get_days_with_events'),
    path('get_eventos_mes/<str:month_year>/', views.get_eventos_mes, name='get_eventos_mes'),
]