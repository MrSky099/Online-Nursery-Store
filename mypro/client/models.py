from django.db import models
from django_countries.fields import CountryField
from nur_admin.models import Nursery , customer

class CartItem(models.Model):
    user_id = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    ordered = models.BooleanField(default=False, null=True)
    product_id = models.ForeignKey(Nursery, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product_id.pro_name}"

    def get_total_item_price(self):
        return self.quantity * self.product_id.price

    class Meta:
        db_table='CartItem'


class Order(models.Model):
    user_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    item = models.ManyToManyField(CartItem)
    total_price = models.FloatField()
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_Address = models.ForeignKey('BillingAddress', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user_id.firstname

    def total(self):
        return sum(item.get_total_item_price() for item in self.item.all())

    class Meta:
        db_table='Order'


class ShippingAddress(models.Model):
    user_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    Street_Address = models.CharField(max_length=100, null=True, blank=True)
    Apartment_Address = models.CharField(max_length=100, null=True, blank=True)
    Countries = CountryField(multiple=False, null=True, blank=True)
    Zip = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    E_mail = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.user_id.firstname

    class Meta:
        db_table='ShippingAddress'

class BillingAddress(models.Model):
    user_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    Street_Address = models.CharField(max_length=100)
    Apartment_Address = models.CharField(max_length=100, null=True, blank=True)
    Countries = models.CharField(max_length=50)
    Zip = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=10)
    E_mail = models.EmailField()


    def __str__(self):
        return self.user_id.firstname

    class Meta:
        db_table='BillingAddress'
