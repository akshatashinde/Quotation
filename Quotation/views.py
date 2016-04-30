from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .forms import QuotationForm,ItemForm
from django.contrib.auth.decorators import login_required
from .models import Quotation, Item
from django.forms import formset_factory

# Create your views here.
def home(request):
	return render(request, 'Quotation/home.html',{})

@login_required(login_url='/admin/login/')
def createitem_formset(request):
	ItemFormSet = formset_factory(ItemForm)
	print 1
	if request.method == 'POST':
		user_form = QuotationForm(request.POST)
		formset = ItemFormSet(request.POST, request.FILES)
		print 2
		if user_form.is_valid() and formset.is_valid() :
			print 3
			quotation_no =  user_form.save()
			print 4
			item = formset.save(commit=False)
			item.quotation_no = quotation_no
			item.total= item.quantity * item.price
			item.save()

			messages.add_message(request, messages.INFO, 'user added details!')
			
			user_form = QuotationForm()
			formset = ItemFormSet()
		else:
			formset.errors
			# HttpResponse('errors availabe on same page...goto the same page again.')

	else:
		user_form = QuotationForm()
		formset = ItemFormSet()

	return render (request,'Quotation/create1.html',{'user_form':user_form, 'formset':formset})			

@login_required(login_url='/admin/login/')
def itemlist(request):
	context = {}
	Quotation_list = Quotation.objects.all()
	
	context = {'Quotation_list':Quotation_list}
	return render(request,'Quotation/view.html',context)

@login_required(login_url='/admin/login/')
def detailitem(request,pk):
	context ={}
	quot = get_object_or_404(Quotation,pk=pk)
	item = Item.objects.all()
	context ={'quot':quot,'item':item}
	return render(request,'Quotation/item_detail.html',context)

@login_required(login_url='admin/login/')
def updateitem(request):
	context={}
	if request.method == 'POST':
		user_form = QuotationForm(data = request.POST)
		item_form = ItemForm(data = request.POST)
		if user_form.is_valid and item_form.is_valid():
			client = request.POST.get('client')
			quotation_no = request.POST.get('quotation_no')
			item = request.POST.get('item')
			quantity = request.POST.get('quantity')
			price = request.POST.get('price')
			
			Quotation.objects.filter(quotation_no=quotation_no).update(
				client=client,
				quotation_no = quotation_no,
				)

			Item.objects.filter(item=item).update(
				item=item,
				quantity=quantity,
				price=price,
				)	

	else:
		user_form = QuotationForm()
		item_form = ItemForm()

	context={'user_form':user_form, 'item_form':item_form}
	return render (request,'Quotation/update.html',context)

@login_required(login_url='/admin/login/')
def createitem(request):
	if request.method == 'POST':
		user_form = QuotationForm(request.POST)
		item_form = ItemForm(request.POST)
		if user_form.is_valid() and item_form.is_valid():
			quotation_no = user_form.save()
			item = item_form.save(commit = False)
			item.quotation_no = quotation_no
			item.total= item.quantity * item.price
			item.save()
			messages.add_message(request, messages.INFO, 'user added details!')

			user_form = QuotationForm()
			item_form = ItemForm()
		else:
			HttpResponse('errors availabe on same page...goto the same page again.')

	else:
		user_form = QuotationForm()
		item_form = ItemForm()

	return render (request,'Quotation/create.html',{'user_form':user_form, 'item_form':item_form})			