from django import forms
from Quotation.models import Quotation,Item


class QuotationForm(forms.ModelForm):
	class Meta:
		model = Quotation
		fields = ['client','quotation_no']

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields =['item','quantity','price']		

	def clean_item(self):
			item = self.cleaned_data['item']

	def clean_quantity(self):
			quantity = self.cleaned_data['quantity']

	def clean_price(self):
			price = self.cleaned_data['price']					