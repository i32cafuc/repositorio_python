from django.db import models
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=255)
	min_price = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=255)
	category = models.ForeignKey(Category)
	image = models.ImageField(upload_to='teams', blank=True, null=True)

	def __str__(self):
		return self.name

class Rider(models.Model):
	name = models.CharField(max_length=255)
	team = models.ForeignKey(Team)
	price = models.IntegerField(default=0)
	price_on_sale = models.IntegerField(default=0)
	salary = models.IntegerField(default=0)
	point = models.IntegerField(default=0)
	valuation = models.IntegerField(default=0)
	damage = models.BooleanField(default=0)
	image = models.ImageField(upload_to='riders', blank=True, null=True)
	
	def __str__(self):
		return self.name
		
	def displayPrice(self):
		return self.price

	def displayPriceOnSale(self):
		return self.price_on_sale

	def displaySalary(self):
		return self.salary

	def updateAfterRace(self,position,point,calc_value,position_no_point):
		if position == 0:
			self.valuation = self.valuation-calc_value
		elif position<position_no_point:
			self.point = self.point + point
			self.valuation = self.valuation+(calc_value/position)
			self.updatePrices(point)
			#TODO actualizar precio y salario del piloto
			self.save()

	def updatePrices(self,point):
		self.price += point*100
		self.price_on_sale += point*50
		self.salary += point*20
		self.save()

	def resetValues(self,margin_sell,margin_salary):
		self.price = self.team.category.min_price
		self.price_on_sale = self.price*margin_sell
		self.salary = self.price*margin_salary
		self.damage = False
		self.valuation = 0
		self.point = 0
		self.save()
		

class Country(models.Model):
	name = models.CharField(max_length=255)
	iso3 = models.CharField(max_length=255)
	color_fill = models.CharField(max_length=255)
	latitude = models.CharField(max_length=255)
	longitude = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Circuit(models.Model):
	name = models.CharField(max_length=255)
	image = models.ImageField(upload_to='circuits', blank=True, null=True)
	def __str__(self):
		return self.name

class Configuration(models.Model):
	name = models.CharField(max_length=255)
	value = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Race(models.Model):
	name = models.CharField(max_length=255)
	circuit = models.ForeignKey(Circuit)
	date_race = models.DateField()
	date_block = models.DateField()
	country = models.ForeignKey(Country)

	def __str__(self):
		return self.name

class League(models.Model):
	name = models.CharField(max_length=255,unique = True)
	rider_on_sale = models.ManyToManyField(Rider, null=True, blank=True, default = None, symmetrical=False)
	def __str__(self):
		return self.name

class Uteam(models.Model):
	name = models.CharField(max_length=255)
	point = models.IntegerField(default=0)
	coin = models.IntegerField(default=0)
	owe = models.IntegerField(default=0)
	loan = models.BooleanField(default=0)
	maintenance = models.BooleanField(default=0)
	enrolment = models.BooleanField(default=0)
	rider = models.ManyToManyField(Rider, null=True, blank=True, default = None, symmetrical=False)
	
	def __str__(self):
		return self.name

	def displayTotalSalary(self):
		riders = Rider.objects.filter(uteam=self)
		salary=0
		for i in riders:
			salary+=i.salary
		return '{:,}'.format(salary)

	def getTotalSalary(self):
		riders = Rider.objects.filter(uteam=self)
		salary=0
		for i in riders:
			salary+=i.salary
		return salary

	def displayCoin(self):
		#return '{:,}'.format(self.coin) 
		return self.coin

	def updateAfterRace(self,point,coin_by_point):
		if self.maintenance and self.enrolment:
			self.point += point
			self.coin += point*coin_by_point
			self.coin -= self.getTotalSalary()
			self.maintenance = False
			self.enrolment = False
			self.save()


class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	uteam = models.ForeignKey(Uteam, null=True, blank=True, default = None)
	debut = models.BooleanField(default=True)
	league = models.ForeignKey(League, null=True, blank=True, default = None)
	def __str__(self):
		return self.user.username