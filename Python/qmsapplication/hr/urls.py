from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from hr import views





urlpatterns = [
    path('hr/', views.Hrlist.as_view()),
    path('hr/<int:pk>/', views.HrDetail.as_view()),

    path('employee/', views.EmployeeView.as_view()),
    path('employee/<int:pk>/', views.EmployeeView.as_view()),

    path('experience/', views.ExpView.as_view()),
    path('experience/<int:pk>/', views.ExpView.as_view()),

    path('competency-matrix/', views.CompetencyView.as_view()),
    path('competency-matrix/<int:pk>/', views.CompetencyView.as_view()),

    path('training-request/', views.TrainingRequestView.as_view()),
    path('training-request/<int:pk>/', views.TrainingRequestView.as_view()),

    path('annual-trainnig/', views.AnnualTrainnigView.as_view()),
    path('annual-trainnig/<int:pk>/', views.AnnualTrainnigView.as_view()),

    path('training-evalution/', views.TrainingEvalutionView.as_view()),
    path('training-evalution/<int:pk>/', views.TrainingEvalutionView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)