import csv

from kolofflinewiki.models import *
from django.db import connection

def delete_table(model):
	name = model._meta.db_table
	model.objects.all().delete()
	cursor = connection.cursor()
	
	sql = "DELETE FROM sqlite_sequence WHERE name = " + "'" + name + "'"
	cursor.execute(sql)

def with_iter(context):
	iterable = context
	with context:
		for value in iterable:
			yield value

def load_tsv(filename):
	return csv.reader(with_iter(open('data/tsv/' + filename , 'r')), delimiter='\t')

def build_item():
	print('building item table')
	delete_table(Item)

	tsv = load_tsv('items.tsv')

	for index, info in enumerate(tsv):
		if index > 0:
			if (index % 100) - 1 == 0:
				print('Saving item line ' + str(index))
			item = Item(
				item_id = int(info[0]),
				name = info[1],
				desc_id = info[2],
				plural = info[3],
				autosell = int(info[4]),
				description = info[5],
				image_src = info[6],
			)
			item.save()

def build_recipe_type():
	print('building recipe type table')
	delete_table(Recipe_type)

	tsv = load_tsv('recipe_type.tsv')

	for index, info in enumerate(tsv):
		if index > 0:
			recipe_type = Recipe_type(
				type_id = int(info[0]),
				name = info[1],
			)
			recipe_type.save()

def build_recipe():
	print('building recipe table')
	delete_table(Recipe)

	tsv = load_tsv('recipe.tsv')

	for index, info in enumerate(tsv):
		if index > 0:
			recipe = Recipe(
				recipe_type = Recipe_type.objects.get(type_id = int(info[0])),
				ingredient_1 = Item.objects.get(item_id = int(info[1])),
				ingredient_2 = Item.objects.get(item_id = int(info[2])),
				result = Item.objects.get(item_id = int(info[3])),
			)
			recipe.save()

def build_db():
	build_item()
	build_recipe_type()
	build_recipe()
