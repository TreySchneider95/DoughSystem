from django.db import models
from django.contrib.auth.models import User


class Unit(models.Model):
    unit = models.CharField(max_length=200)

class InventoryRaw(models.Model):
    name = models.CharField(max_length=200)
    qty = models.FloatField()
    unit_used = models.ForeignKey(Unit, on_delete=models.CASCADE)

class Purchase(models.Model):
    date_purchased = models.DateField()
    price = models.FloatField()
    where = models.CharField(max_length=200)
    product = models.ForeignKey(InventoryRaw, on_delete=models.CASCADE)
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