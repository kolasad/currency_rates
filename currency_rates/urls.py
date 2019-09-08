from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from reports.views import ReportApiView


router = SimpleRouter()
router.register('api/report', ReportApiView, basename='reports')

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls

