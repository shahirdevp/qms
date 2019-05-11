from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from formation import views





urlpatterns = [
    path('cformation/', views.CformationViewset.as_view()),
    path('cformation/<int:pk>/', views.CformationViewset.as_view()),

   

   
]

