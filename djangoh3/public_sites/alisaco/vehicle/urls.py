from django.urls import path
from .views import *

urlpatterns = [
		path('', VehicleListView.as_view()),
		path('vehicle/new', VehicleCreateView.as_view()),
		path('vehicle/<int:pk>/delete', VehicleDeleteView.as_view()),
		path('vehicle/<int:pk>', VehicleUpdateView.as_view()),
]
