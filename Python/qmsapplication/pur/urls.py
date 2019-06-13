from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from pur import views





urlpatterns = [
    path('supplier/', views.Supplier.as_view()),
    path('supplier/<int:pk>/', views.Supplier.as_view()),

    path('purchase-approved-supplier/', views.PurchaseApprovedSupplier.as_view()),
    path('purchase-approved-supplier/<int:pk>/', views.PurchaseApprovedSupplier.as_view()),

    path('purchase-order/', views.PurchaseOrder.as_view()),
    path('purchase-order/<int:pk>/', views.PurchaseOrder.as_view()),

    path('goods-recipt/', views.GoodsRecipt.as_view()),
    path('goods-recipt/<int:pk>/', views.GoodsRecipt.as_view()),

    path('stock-register/', views.StockRegister.as_view()),
    path('stock-register/<int:pk>/', views.StockRegister.as_view()),

    path('approved-suppliers/', views.ApprovedSupplierPurchase.as_view()),

]

