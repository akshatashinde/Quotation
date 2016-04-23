from django import template

register = template.Library()
from Quotation.models import Quotation,Item

def get_item(value):
	try:
		profile = Quotation.objects.get(quotation_no = value)
		print profile,value
		data = Item.objects.filter(quotation_no = profile)
		print data
	except:
		data = []
	return data

register.filter('get_item', get_item)