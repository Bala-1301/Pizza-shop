from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.BigIntegerField()
	state = models.CharField(max_length=64, null=True)
	city = models.CharField(max_length=64, null=True)
	area = models.CharField(max_length=64, null=True)
	street = models.CharField(max_length=64, null=True)
	doorNo = models.IntegerField(null=True)

	def __str__(self):
		return f"{self.user.username}"


class Topping(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}" 

class Pizza(models.Model):
	name = models.CharField(max_length=64)
	smallPrice = models.DecimalField(max_digits=7, decimal_places=2)
	largePrice = models.DecimalField(max_digits=7, decimal_places=2)
	oneToppingSmall = models.DecimalField(max_digits=7, decimal_places=2)
	twoToppingsSmall = models.DecimalField(max_digits=7, decimal_places=2)
	threeToppingsSmall = models.DecimalField(max_digits=7, decimal_places=2)
	oneToppingLarge = models.DecimalField(max_digits=7, decimal_places=2)
	twoToppingsLarge = models.DecimalField(max_digits=7, decimal_places=2)
	threeToppingsLarge = models.DecimalField(max_digits=7, decimal_places=2)
	specialSmall = models.DecimalField(max_digits=7, decimal_places=2)
	specialLarge = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return f"{self.name} | S ₹{self.smallPrice} | L ₹{self.largePrice}"
	
class ExtraCheese(models.Model):
	price = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return f"ExtraCheese | ₹{self.price}"

class Sub(models.Model):
	name = models.CharField(max_length=64)
	smallPrice = models.DecimalField(max_digits=7, decimal_places=2)
	largePrice = models.DecimalField(max_digits=7, decimal_places=2)
	extraCheese = models.ForeignKey(ExtraCheese, on_delete=models.CASCADE)
	
	def __str__(self):
		return f"{self.name} | S ₹{self.smallPrice} | L ₹{self.largePrice}"

class Extra(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(default=10,max_digits=7, decimal_places=2)	

	def __str__(self):
		return f"{self.name} | ₹{self.price}"

class SubWithExtra(models.Model):
	sub = models.OneToOneField(Sub, on_delete=models.CASCADE, null=True)
	extras_id = models.ForeignKey(Extra, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return f"{self.sub.name}| S ₹{self.sub.smallPrice} | L ₹{self.sub.largePrice}" 

class Pasta(models.Model):
	name = models.CharField(max_length=64)
	
	def __str__(self):
		return f"{self.name}"

class Serving(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"

class PastaWithServing(models.Model):
	pasta_id = models.ForeignKey(Pasta, on_delete=models.CASCADE)
	Servings_id = models.ForeignKey(Serving, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
	 return f"{self.pasta_id.name} with {self.Servings_id.name}"

class Salad(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return f"{self.name} | ₹{self.price}"

class DinnerPlatter(models.Model):
	name = models.CharField(max_length=64)
	smallPrice = models.DecimalField(max_digits=7, decimal_places=2)
	largePrice = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return f"{self.name} | ₹{self.smallPrice} | L ₹{self.largePrice}"