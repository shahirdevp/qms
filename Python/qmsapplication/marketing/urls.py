from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from marketing import views





urlpatterns = [
    path('enquery-register/', views.EqRegister.as_view()),
    path('enquery-register/<int:pk>/', views.EqRegister.as_view()),

    path('technicall-feasiblity/', views.TecFeasiblity.as_view()),
    path('technicall-feasiblity/<int:pk>/', views.TecFeasiblity.as_view()),

    path('marketing-feasibility/', views.MktFeasiblity.as_view()),
    path('marketing-feasibility/<int:pk>/', views.MktFeasiblity.as_view()),


    path('quality-feasibility/', views.QltFeasiblity.as_view()),
    path('quality-feasibility/<int:pk>/', views.QltFeasiblity.as_view()),


    path('reviewer/', views.Review.as_view()),
    path('reviewer/<int:pk>/', views.Review.as_view()),

    path('configuration-management-report/', views.ConfMR.as_view()),
    path('configuration-management-report/<int:pk>/', views.ConfMR.as_view()),
]

