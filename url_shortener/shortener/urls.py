from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name='shorten_url'),
    path('<str:short_code>/', views.expand_url, name='expand_url'),
]
