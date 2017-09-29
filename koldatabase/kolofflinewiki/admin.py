# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Item, Recipe, Recipe_type

admin.site.register(Item)
admin.site.register(Recipe)
admin.site.register(Recipe_type)

# Register your models here.
