from django.db import models
from django.contrib.auth.models import User


class Unit(models.Model):
    unit = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.unit}"

class InventoryRaw(models.Model):
    name = models.CharField(max_length=200)
    qty = models.FloatField(default=0)
    unit_used = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
    def take_inventory(self, qty, unit):
        purchase_to_take_from = self.purchases.filter(qty_left__gt = 0).latest('date_purchased')

class Purchase(models.Model):
    date_purchased = models.DateField()
    price = models.FloatField()
    where = models.CharField(max_length=200)
    product = models.ForeignKey(InventoryRaw, on_delete=models.CASCADE, related_name="purchases")
    qty_purchased = models.FloatField()
    qty_left = models.FloatField()
    refrigerated = models.BooleanField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    person_who_purchased = models.ForeignKey(User, on_delete=models.CASCADE)


class RecipeIngrediant(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('InventoryRaw', on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(InventoryRaw, through=RecipeIngrediant)
    amount_made = models.FloatField()
    amount_made_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    person_made = models.ForeignKey(User, on_delete=models.CASCADE)

class Dough(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    qty = models.FloatField()
    date_made = models.DateField(auto_now=True)
    price_per_scoop = models.FloatField()
    active = models.BooleanField(default=True)

class Calcs(models.Model):
    one_to_convert = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="one_to_convert")
    base = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="base")
    conversion = models.FloatField()

    def __str__(self):
        return f"{self.one_to_convert.unit}s to {self.base.unit}s"