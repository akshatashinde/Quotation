from django.db import models

# Create your models here.

class Quotation(models.Model):
	client = models.CharField(max_length=200)
	quotation_no = models.IntegerField(unique=True)
	# quotation_no = models.AutoField(primary_key=True)

	def __unicode__(self):
		return self.client

class Item(models.Model):
	quotation_no= models.ForeignKey(Quotation,null=True,blank=True)
	item = models.CharField(max_length=200)
	quantity = models.IntegerField(default='0')
	price = models.FloatField()
	total = models.FloatField()

	def __unicode__(self):
		return self.item