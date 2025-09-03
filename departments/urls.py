from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewset

router = DefaultRouter()
router.register(r'departments', DepartmentViewset)

urlpatterns = [
    path('', include(router.urls)),
]