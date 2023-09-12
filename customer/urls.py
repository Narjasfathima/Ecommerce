from django.urls import path
from .views import *



urlpatterns=[
    
    path('custhome',HomeView.as_view(),name="cust_home"),
    path("prodetail/<int:pid>",ProductView.as_view(),name="pdtview"),
    path('addcart/<int:id>',add_cart,name='add_cart'),
    path('cart_list',CartListView.as_view(),name="cart_list"),
    path('cartdelete/<int:cid>',cart_remove,name="cart_dlt"),
    path('checkout/<int:cid>',CheckoutView.as_view(),name='checkout'),
    path('orderlist',OrderListView.as_view(),name='order_list'),
    path('corder/<int:id>',cancel_order,name='c_order'),
    path('dorder/<int:id>',rem_order,name='d_order')

]