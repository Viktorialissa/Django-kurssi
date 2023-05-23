from django.views.generic import TemplateView, ListView
from .models import *

#class GarmentView(TemplateView):
#		template_name = "clothes/garment.html"

class GarmentListView(ListView):
        model = Garment
