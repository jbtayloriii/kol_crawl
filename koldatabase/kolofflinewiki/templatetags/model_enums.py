from django import template

register = template.Library()

@register.filter
def recipe_type_image(value):
	#meat pasting
	html = '<a href="link"><img src="image" /></a>'
	if value == 1:
		return html.replace('link', 'test').replace('image', '/kolofflinewiki/item_images/wad.gif')
