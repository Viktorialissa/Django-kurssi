from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegisterView(CreateView):
	form_class = UserCreationForm
	template_name = "registration/register.html"
	success_url = "/"

class DiaryView(TemplateView):
	template_name = "sportdiary/about.html"

class DiaryListView(LoginRequiredMixin, ListView):
	model = Diary
	template_name = "diary_list.html"

	def get_queryset(self):
			return Diary.objects.filter(owner=self.request.user)
	

class DiaryUpdateView(UserPassesTestMixin, UpdateView):
	model = Diary
	fields = ["name", "duration", "description", "location"]
	success_url = "/"

	def test_func(self):
			return self.request.user.is_authenticated
		

class DiaryCreateView(LoginRequiredMixin, CreateView):
	model = Diary
	fields = ["name", "duration", "description", "location"]
	success_url = "/"

	def form_valid(self, form):
			form.instance.owner = self.request.user
			return super().form_valid(form)

class DiaryDeleteView(UserPassesTestMixin, DeleteView):
	model = Diary
	success_url = "/"

	def test_func(self):
			workout = self.get_object()
			return self.request.user == workout.owner
	

class LocationListView(LoginRequiredMixin, ListView):
	model = Location
	

class LocationCreateView(LoginRequiredMixin, CreateView):
	model = Location
	fields = ["name"]
	success_url = "/"
