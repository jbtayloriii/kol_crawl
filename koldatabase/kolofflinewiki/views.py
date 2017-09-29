# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Item, Recipe

def index(request):
	return HttpResponse('Hello world')

#TODO: make this prettier, right now it's just debug
def item_list(request):
	item_list = Item.objects.order_by('item_id')
	return render(request, 'kolofflinewiki/items.html', {'item_list': item_list})

def get_recipes_with_ingredient(item, recipe_type = None):
	q1 = Recipe.objects.filter(ingredient_1 = item.item_id)
	q2 = Recipe.objects.filter(ingredient_2 = item.item_id)

	set = q1.union(q2)

	if not recipe_type is None:
		set = set.filter(recipe_type = recipe_type)
	return set

def item_detail(request, item_id):
	item = get_object_or_404(Item, item_id=item_id)

	recipe_ingredient = get_recipes_with_ingredient(item)
	return render(request, 'kolofflinewiki/item_detail.html', {
		'item': item,
		'recipe_ingredient' : recipe_ingredient
	})
