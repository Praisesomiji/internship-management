from rest_framework import viewsets
from .models import Activity, Category, Trace
from .serializers import ActivitySerializer, CategorySerializer, TraceSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TraceViewSet(viewsets.ModelViewSet):
    queryset = Trace.objects.all()
    serializer_class = TraceSerializer

