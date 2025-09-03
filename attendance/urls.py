from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewset

router = DefaultRouter()
router.register(r'attendance', AttendanceViewset)

urlpatterns = [
    path('', include(router.urls)),
]