from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.portfolio_main, name='portfolio_main'),
    path('create/', views.portfolio_create, name='portfolio_create'),
    path('update/<int:id>/', views.portfolio_update, name='portfolio_update'),
]
