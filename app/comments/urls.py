from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    path('boom/', views.boom, name='boom'),
]
