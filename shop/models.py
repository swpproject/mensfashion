from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=500,unique=True)
    slug = models.SlugField(null=True,blank=True,max_length=250,unique=True)

    def __str__(self):
        return  f"{self.slug}"

class Product(models.Model):
    name = models.CharField(max_length = 500,unique=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    feature = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    slug = models.SlugField(null=True,blank=True,max_length=250)
    description = models.TextField()
    specifications = models.TextField()
    category = models.ForeignKey(to=Category,on_delete=CASCADE,null=True, blank=True)
    stock = models.IntegerField(default=10)
    img1=models.ImageField(upload_to = "products", null=True)
    img2=models.ImageField(upload_to = "products", null=True)
    img3=models.ImageField(upload_to = "products", null=True)

    def __str__(self):
        return f"{self.id}"

class Order(models.Model):
    customer = models.ForeignKey(to=User,on_delete=CASCADE,null=True, blank=True)
    firstname=models.CharField(max_length=500,default='')
    lastname=models.CharField(max_length=500,default='')
    email=models.CharField(max_length=500,default='')
    mobile=models.CharField(max_length=12,default='')
    address=models.CharField(max_length=1000,default='')
    country=models.CharField(max_length=50,default='')
    state=models.CharField(max_length=50,default='')
    zipcode=models.CharField(max_length=20,default='')
    paymenttype=models.CharField(max_length=50,default='')
    Total = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.id}"



cart_status =(
    ("In Process", "In Process"),
    ("Packing", "Packing"),
    ("Out For Delivery", "Out For Delivery"),
    ("Delivered", "Delivered"),
    ("Cancel", "Cancel"),
    ("Return", "Return"),
)

class Cart(models.Model):
    order = models.ForeignKey(to=Order,on_delete=CASCADE,null=True,blank=True)
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(to=User,on_delete=CASCADE,null=True, blank=True)
    product = models.ForeignKey(to=Product,on_delete=CASCADE,null=True, blank=True)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    status = models.CharField(choices = cart_status,default='In Process',max_length = 100 )

    def __str__(self):
        return  f"{self.id}"


class CancelOrder(models.Model):
    user = models.ForeignKey(to=User,on_delete=CASCADE,null=True, blank=True)
    oid=models.CharField(null=True, blank=True,max_length=500)
    message = models.TextField()