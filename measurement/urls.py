from django.contrib import admin
from django.urls import path
from measurement.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorListCreateAPIView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementCreateAPIView.as_view()),
]
