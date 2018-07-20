from django.urls import path

from . import views

app_name = 'observation'

urlpatterns = [
    path('add/', views.add, name='add')
]