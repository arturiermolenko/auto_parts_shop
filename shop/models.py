from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Item(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=6, unique=True)
    description = models.TextField()
    materials = models.CharField(max_length=255)
    quantity = models.IntegerField()
    costs_prise = models.DecimalField(max_digits=16, decimal_places=2)
    sell_price = models.DecimalField(max_digits=16, decimal_places=2)
    link_where_buy = models.TextField()
    
    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.number} {self.name}"
    
