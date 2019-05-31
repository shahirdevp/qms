from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from formation import views





urlpatterns = [
    path('cformation/', views.CformationViewset.as_view()),
    path('cformation/<int:pk>/', views.CformationViewset.as_view()),

    path('process/', views.CprocessViewset.as_view()),
    path('process/<int:pk>/', views.CprocessViewset.as_view()),
    path('process-cmp/<int:CmpName>/', views.CprocessCmpViewset.as_view(), name="Company process list"),

    path('policy/', views.PolicyViewset.as_view(), name='file-upload'),
    path('admin-register/', views.CreateUserView.as_view(), name='Create admin'),

   path('org-process-chart', views.OrgProcessChartViewset.as_view(), name="org process chart"),
   path('org-process-chart/<int:pk>', views.OrgProcessChartViewset.as_view(), name="single org process chart "),

]

