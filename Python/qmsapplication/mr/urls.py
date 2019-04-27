from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from mr import views





urlpatterns = [
    path('mr/doc-type/', views.DocTypeView.as_view()),
    path('mr/doc-type/<int:pk>/', views.DocTypeView.as_view()),

    path('mr/internal-external-docs/', views.InterExternView.as_view()),
    path('mr/internal-external-docs/<int:pk>/', views.InterExternView.as_view()),

    path('mr/internal-audit-plan/', views.InternalAuditPlanView.as_view()),
    path('mr/internal-audit-plan/<int:pk>/', views.InternalAuditPlanView.as_view()),

    path('mr/internal-audit-report/', views.InternalAuditReportView.as_view()),
    path('mr/internal-audit-report/<int:pk>/', views.InternalAuditReportView.as_view()),

    path('mr/non-conf/', views.NonConfView.as_view()),
    path('mr/non-conf/<int:pk>/', views.NonConfView.as_view()),
]

