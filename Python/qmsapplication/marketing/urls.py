from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from marketing import views





urlpatterns = [
    
    path('mkt/enquery-register', views.Hrlist.as_view()),
]