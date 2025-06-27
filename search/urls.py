from django.urls import path

from . import views

urlpatterns = [
    path('get_quicksearch/<str:data>/', views.get_quicksearch, name='get_quicksearch'),
    path('ie-check/<str:data>/', views.ie_check, name='ie_check'),
]