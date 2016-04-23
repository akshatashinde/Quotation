from django.conf.urls import include, url
from django.contrib import admin
from Quotation import views

app_name='Quotation'
urlpatterns = [
	url(r'^$',views.home, name='home'),
	url(r'^create/$', views.createitem, name='create_item'),
	url(r'^list/$',views.itemlist, name='list_item'),
	url(r'^(?P<pk>[0-9]+)/$',views.detailitem, name='item_detail'),	
	url(r'^update/$',views.updateitem, name='update_item'),
	]
	