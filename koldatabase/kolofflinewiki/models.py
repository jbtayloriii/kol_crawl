# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
	item_id = models.IntegerField(default=0, primary_key=True)
	name = models.CharField(max_length=200)
	desc_id = models.CharField(max_length=200)
	plural = models.CharField(max_length=200)
	autosell = models.IntegerField(default=0)
	description = models.CharField(max_length=500)
	image_src = models.CharField(max_length=200)

	def __str__(self):
		return str(self.item_id) + ': ' + self.name;

class Recipe_type(models.Model):
	type_id = models.IntegerField(default=0, primary_key=True)
	name = models.CharField(max_length=200)

	def __str__(self):
		return str(self.name)

class Recipe(models.Model):
	recipe_type = models.ForeignKey(Recipe_type, on_delete=models.CASCADE)
	ingredient_1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='ingredient_1')
	ingredient_2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='ingredient_2')
	result = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='result')
