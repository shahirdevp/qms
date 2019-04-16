from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from marketing import views





urlpatterns = [
    path('mkt/enquery-register/', views.EqRegister.as_view()),
    path('mkt/enquery-register/<int:pk>/', views.EqRegister.as_view()),

    path('mkt/technicall-feasiblity/', views.TecFeasiblity.as_view()),
    path('mkt/technicall-feasiblity/<int:pk>/', views.TecFeasiblity.as_view()),

    path('mkt/quality-feasibility/', views.MktFeasiblity.as_view()),
    path('mkt/quality-feasibility/<int:pk>/', views.MktFeasiblity.as_view()),


    path('mkt/marketing-feasibility/', views.QltFeasiblity.as_view()),
    path('mkt/marketing-feasibility/<int:pk>/', views.QltFeasiblity.as_view()),


    path('mkt/reviewer/', views.Review.as_view()),
    path('mkt/reviewer/<int:pk>/', views.Review.as_view()),

    path('mkt/configuration-management-report/', views.ConfMR.as_view()),
    path('mkt/configuration-management-report/<int:pk>/', views.ConfMR.as_view()),
]

