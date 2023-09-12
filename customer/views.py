from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect

from django.views.generic import TemplateView,ListView,DetailView

from account.models import Product,Cart,Order

from django.contrib import messages

from account.views import signin_required

from django.utils.decorators import method_decorator

from account.views import decs

# Create your views here.

# 1) HOME
@method_decorator(decs,name="dispatch")
class HomeView(ListView):
    template_name="cust_home.html"
    queryset=Product.objects.all()
    context_object_name="pdt"


# 2) PRODUCT VIEW

@method_decorator(decs,name="dispatch")
class ProductView(DetailView):
    template_name="prodetail.html"
    queryset=Product.objects.all()
    pk_url_kwarg="pid"
    context_object_name="data"


# 3) ADDED TO CART
decs
def add_cart(request,*args,**kwargs):
    pid=kwargs.get('id')
    pro=Product.objects.get(id=pid)
    user=request.user
    qty=request.POST.get('qty')
    Cart.objects.create(product=pro,user=user,quantity=qty)
    messages.success(request,"Product added to cart!!")
    return redirect('cust_home')


# 4) CART VIEW
@method_decorator(decs,name="dispatch")
class CartListView(ListView):
    template_name="cart_list.html"
    queryset=Cart.objects.all()
    context_object_name="cart"

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user,status='cart')
    

# 5) DELETE CART ITEM
decs
def cart_remove(request,*args,**kwargs):
    id=kwargs.get('cid')
    res=Cart.objects.get(id=id)
    res.delete()
    messages.success(request,"Item removed from cart!!")
    return redirect('cart_list')

# 5) ORDER CART ITEM
@method_decorator(decs,name="dispatch")
class CheckoutView(TemplateView):
    template_name="checkout.html"

    def post(self,request,*args,**kwargs):
        cid=kwargs.get('cid')
        cart=Cart.objects.get(id=cid)
        prod=cart.product
        user=request.user
        qty=cart.quantity
        addr=request.POST.get('address')
        ph=request.POST.get('phone')
        Order.objects.create(product=prod,user=user,address=addr,phone=ph,quantity=qty)
        cart.status="order placed"
        cart.save()
        messages.success(request,"order placed!!!")
        return redirect('cart_list')
    
# 6) ORDER list
@method_decorator(decs,name="dispatch")
class OrderListView(ListView):
    template_name="order_list.html"
    queryset=Order.objects.all()
    context_object_name="order"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

# 7) CANCEL ORDER 
decs
def cancel_order(request,*args,**kwargs):
    id=kwargs.get('id')
    res=Order.objects.get(id=id)
    res.status='order canceled'
    res.save()
    messages.success(request,"Order canceled!!!")
    return redirect('order_list')

decs
def rem_order(request,**kwargs):
    id=kwargs.get('id')
    res=Order.objects.get(id=id)
    res.delete()
    messages.success(request,"Order deleted")
    return redirect('order_list')