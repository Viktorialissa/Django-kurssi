from django.db import models

class Garment(models.Model):
    COLOR_CHOICES = [
            ('PUNAINEN', 'Punainen'),
            ('MUSTA', 'Musta'),
            ('SININEN', 'Sininen'),
            ('VALKOINEN', 'Valkoinen'),
            ('KELTAINEN', 'Keltainen'),
            ('VIHREÄ', 'Vihreä'),
        ]

    name = models.CharField(max_length=200)
    color = models.CharField(blank=True, choices=COLOR_CHOICES, max_length=20)

    def __str__(self):
        if self.color:
            return f"{self.name} - {self.get_color_display()}"
        else:
            return self.name

