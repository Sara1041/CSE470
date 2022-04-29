from django.test import TestCase
from .models import Customer, Tag, Product, Order


# Create your tests here.
class TestCustomer(TestCase):
	def test_customer_creation(self):
		customer=Customer.objects.create(name="Ahad", phone="01976547824", email="ahad@gmail.com")
		assert Customer.objects.count()==1
		assert Customer.objects.latest("id").name=="Ahad"

class TestTag(TestCase):
	def test_tag_creation(self):
		tag=Tag.objects.create(name="Decorative")
		tag=Tag.objects.create(name="Beauty Products")
		assert Tag.objects.count()==2
		assert Tag.objects.latest("id").name=="Beauty Products"

class TestProduct(TestCase):
	def test_product_creation(self):
		product=Product.objects.create(name="Keyboard", price=500.0, category="Indoor", description="Bought 1 year ago")
		assert Product.objects.count()==1
		assert Product.objects.latest("id").name=="Keyboard"

class TestOrder(TestCase):
	def test_order_creation(self):
		order=Order.objects.create(status="Pending", note="None")
		assert Order.objects.count()==1
		assert Order.objects.latest("id")