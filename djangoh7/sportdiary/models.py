from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import pytz

class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
             return self.name

class Diary(models.Model):
	name = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True, null=True)
	duration = models.IntegerField(blank=True, null=True)
	description = models.TextField(blank=True)
	location = models.ForeignKey(
		Location, on_delete=models.CASCADE,
		null=True, blank=True,
		related_name='locations'
	)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
			return self.name

	def save(self):
	        self.created = timezone.now()
	        super().save()
