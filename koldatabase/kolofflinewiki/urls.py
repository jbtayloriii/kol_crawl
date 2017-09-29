from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^items/$', views.item_list, name='item_list'),
	url(r'^item/(?P<item_id>[0-9]+)/$', views.item_detail, name='item_detail')
]
