from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
             return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (f"{self.name} {self.manufacturer}")
        
