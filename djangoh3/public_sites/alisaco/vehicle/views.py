from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *

#class VehicleView(TemplateView):
#		template_name = "vehicle/vehicle.html"
class VehicleListView(ListView):
        model = Vehicle

class VehicleUpdateView(UpdateView):
        model = Vehicle
        fields = ["name", "weight", "description"]
        success_url = "/"

class VehicleCreateView(CreateView):
        model = Vehicle
        fields = ["name", "weight", "description"]
        success_url = "/"

class VehicleDeleteView(DeleteView):
        model = Vehicle
        success_url = "/"
