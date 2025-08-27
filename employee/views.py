from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import DepartmentSerializer, EmployeeSerializer, AttendanceSerializer, PerformanceSerializer
from .models import Employee, Department, Attendance, Performance
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd
from django.db.models import Count

# Create your views here.

class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data= request.data, context = {'request': request})
        serializer.is_valid(raise_exception= True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Dept', 'Date_of_join']
    permission_classes = [permissions.IsAuthenticated]

class AttendanceViewset(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class PerformanceViewset(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [permissions.IsAuthenticated]


# Generating Pie chart employees per departments 
def Chart(request):

    # --------------------------
    #  Employee per Department
    # --------------------------

    # Fetch data 
    Employees = Employee.objects.values('Dept__Name').annotate(count = Count('id'))
    departments = [dept['Dept__Name'] for dept in Employees]
    employee_count = [e['count'] for e in Employees]

    pie = px.pie(names=departments, values=employee_count, 
                 title = "Employee per Department", 
                 color_discrete_sequence=px.colors.sequential.RdBu)
    


    pie_div = plot(pie, output_type='div', include_plotlyjs=False)


    # ------------------------------
    #   Monthly attendance overview
    # ------------------------------

    atd = Attendance.objects.values()
    df = pd.DataFrame(list(atd))

    if df.empty:
        bar_div = "<h3>No attendance data available.</h3>"
    else:
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
    
        # Group by month and count records
        monthly_counts = df.resample('M').size()

        # Create the Bar Chart figure
        bar = px.bar(x=monthly_counts.index, 
                     y=monthly_counts.values, 
                     title="Monthly Attendeance Overview",
                     )
        bar.update_layout(xaxis_title="Month",
            yaxis_title="Number of Records")
        
        bar_div = plot(bar, output_type='div', include_plotlyjs=False)

    # Pass the charts to the template context
    context = {
        'pie_chart': pie_div,
        'bar_chart': bar_div,
    }
    
    return render(request, 'chart.html', context)
    