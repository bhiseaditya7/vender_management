from django.contrib import admin
from django.urls import path
from firstApp import views


urlpatterns = [
    path('',views.index),
    path('vender/',views.VenderList.as_view()),
    path('PO/',views.PurchaseOrderList.as_view()),
    path('vender/<int:pk>',views.VenderDetails.as_view()),
    path('PO/<int:pk>',views.PurchaseOrderDetails.as_view()),
    path('vender/<int:pk>/performance',views.Performance.as_view()),
    
]
