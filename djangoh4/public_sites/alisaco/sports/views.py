from django.shortcuts import render

from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from .models import *

#class EquipmentView(TemplateView):
#        template_name = "sports/equipment.html"

class RegisterView(CreateView):
	form_class = UserCreationForm
	template_name = "registration/register.html"
	success_url = "/"

		
class EquipmentListView(LoginRequiredMixin, ListView):
	model = Equipment
	template_name = "equipment_list.html"

	def get_queryset(self):
	        return Equipment.objects.filter(owner=self.request.user)

				
class EquipmentUpdateView(UserPassesTestMixin, UpdateView):
	model = Equipment
	fields = ["name","price", "description", "manufacturer"]
	success_url = "/"

	def test_func(self):
	        return self.request.user.is_authenticated
		

class EquipmentCreateView(LoginRequiredMixin, CreateView):
	model = Equipment
	fields = ["name", "price", "description", "manufacturer"]
	success_url = "/"

	def form_valid(self, form):
	        form.instance.owner = self.request.user
	        return super().form_valid(form)

		

class EquipmentDeleteView(UserPassesTestMixin, DeleteView):
	model = Equipment
	success_url = "/"

	def test_func(self):
	        equipment = self.get_object()
	        return self.request.user == equipment.owner

		

class ManufacturerListView(LoginRequiredMixin, ListView):
	model = Manufacturer

		
class ManufacturerUpdateView(UserPassesTestMixin, UpdateView):
	model = Manufacturer
	fields = ["name"]
	success_url = "/"

	def test_func(self):
	        return self.request.user.is_authenticated

		

class ManufacturerCreateView(LoginRequiredMixin, CreateView):
	model = Manufacturer
	fields = ["name"]
	success_url = "/"

	   
