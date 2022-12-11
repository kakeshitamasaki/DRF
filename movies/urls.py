from django.contrib import admin
from django.urls import path
from . import views

app_name ='movies'

urlpatterns = [
    path('products/',views.ProductListView.as_view(),name='products'),
]