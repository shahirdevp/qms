from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from pur import views





urlpatterns = [
    path('pur/supplier/', views.Supplier.as_view()),
    path('pur/supplier/<int:pk>/', views.Supplier.as_view()),

    path('pur/purchase-approved-supplier/', views.PurchaseApprovedSupplier.as_view()),
    path('pur/purchase-approved-supplier/<int:pk>/', views.PurchaseApprovedSupplier.as_view()),

    path('pur/purchase-order/', views.PurchaseOrder.as_view()),
    path('pur/purchase-order/<int:pk>/', views.PurchaseOrder.as_view()),

    path('pur/goods-recipt/', views.GoodsRecipt.as_view()),
    path('pur/goods-recipt/<int:pk>/', views.GoodsRecipt.as_view()),

    path('pur/stock-register/', views.StockRegister.as_view()),
    path('pur/stock-register/<int:pk>/', views.StockRegister.as_view()),

   
]

