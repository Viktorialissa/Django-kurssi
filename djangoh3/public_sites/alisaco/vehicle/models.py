from django.db import models

class Vehicle(models.Model):
   name = models.CharField(max_length=200)
   weight = models.FloatField(blank=True, null=True)
   description = models.TextField(blank=True)

   def __str__(self):
         return self.name
