from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
		path('', EquipmentListView.as_view()),
		path('equipment/<int:pk>', EquipmentUpdateView.as_view()),
		path('equipment/new', EquipmentCreateView.as_view()),
		path('equipment/<int:pk>/delete', EquipmentDeleteView.as_view()),
		path('manufacturer/<int:pk>', ManufacturerUpdateView.as_view()),
		path('manufacturer/new', ManufacturerCreateView.as_view()),
		path('accounts/login/', LoginView.as_view()),
		path('logout/', LogoutView.as_view(next_page="/"))
		
		
]
