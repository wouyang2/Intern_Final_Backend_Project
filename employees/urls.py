from django.urls import include, path
from .views import EmployeeViewset, PerformanceViewset, AuthToken, Chart
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employee', EmployeeViewset)
#router.register(r'department', DepartmentViewset)
#router.register(r'attendance', AttendanceViewset)
router.register(r'performance', PerformanceViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', AuthToken.as_view(), name='api_token_auth'),
    path('chart/', Chart, name='chart'),
]
