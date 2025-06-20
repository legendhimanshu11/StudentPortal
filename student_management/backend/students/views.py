from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        try:
            student = Student.objects.get(username=username, email=email)
            return render(request, 'dashboard.html', {'student': student})
        except Student.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer