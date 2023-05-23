from django.urls import path
from .views import *

urlpatterns = [
    path('', GarmentListView.as_view()),
]
