from account.models import Cart,Order

def cart_count(request):
    if request.user.is_authenticated:
        ccount=Cart.objects.filter(user=request.user,status='cart').count()
        return {'ccount':ccount}
    else:
        return {'ccount':0}

def order_count(request):
    if request.user.is_authenticated:
        ocount=Order.objects.filter(user=request.user).count()
        return {'ocount':ocount}
    else:
        return {'ocount':0}