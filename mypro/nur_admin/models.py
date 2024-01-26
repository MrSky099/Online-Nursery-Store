from django.db import models
class Nursery(models.Model):
    pro_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    file = models.FileField()
    class Meta:
        db_table = 'Nursery'

class customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=12)
    password = models.IntegerField()
    c_password = models.IntegerField()
    is_admin = models.IntegerField(default=0)
