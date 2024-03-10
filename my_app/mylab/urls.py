from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('taxrate/', views.taxrate, name='taxrate'),
    path('<str:price>/', views.anyNumber, name='anyNumber'),
]
