from django.urls import path, include
from rest_framework import routers
from hr.api.viewsets import HrViewSet


router = routers.DefaultRouter()
router.register('', HrViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
