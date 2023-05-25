from django.shortcuts import render

from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#class EquipmentView(TemplateView):
#        template_name = "sports/equipment.html"
        

		
class EquipmentListView(LoginRequiredMixin, ListView):
        model = Equipment
        
class EquipmentUpdateView(LoginRequiredMixin, UpdateView):
        model = Equipment
        fields = ["name","price", "description", "manufacturer"]
        success_url = "/"

class EquipmentCreateView(LoginRequiredMixin, CreateView):
        model = Equipment
        fields = ["name", "price", "description", "manufacturer"]
        success_url = "/"

class EquipmentDeleteView(LoginRequiredMixin, DeleteView):
        model = Equipment
        success_url = "/"

class ManufacturerUpdateView(LoginRequiredMixin, UpdateView):
        model = Manufacturer
        fields = ["name"]
        success_url = "/"

class ManufacturerCreateView(LoginRequiredMixin, CreateView):
        model = Manufacturer
        fields = ["name"]
        success_url = "/"
