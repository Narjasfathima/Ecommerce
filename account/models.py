from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100)
    descripion=models.CharField(max_length=500)
    image=models.ImageField(upload_to="product_images")
    price=models.IntegerField()
    options=(
        ('Mobile Phone','Mobile Phone'),
        ('Tablets','Tablets'),
        ('Smart Watch','Smart Watch'),
        ('BT Speakers','BT Speakers')
    )
    category=models.CharField(max_length=100,choices=options)



class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default='cart')
    quantity=models.IntegerField(null=True)

    @property
    def total_amnt(self):
        tot=self.product.price*self.quantity
        return tot




class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ("order placed","order placed"),
        ("shipped","shipped"),
        ("order pending","order pending"),
        ("out for delivery","out for delivery"),
        ("delivered","delivered"),
        ("order canceled","order canceled")
    )
    status=models.CharField(max_length=100,choices=options,default='order placed')
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    quantity=models.IntegerField(default=1)