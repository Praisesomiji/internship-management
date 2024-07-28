"""
URL configuration for internship_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from members.views import ProfileViewSet
from teams.views import TeamViewSet, UnitViewSet
from products.views import ProductViewSet, ProductionViewSet
from activities.views import ActivityViewSet, CategoryViewSet, TraceViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'units', UnitViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productions', ProductionViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'traces', TraceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

