from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.views.generic import View,CreateView,FormView

from django.urls import reverse_lazy

from .forms import *

from django.contrib import messages

from django.contrib.auth import login,logout,authenticate

from django.utils.decorators import method_decorator

from django.views.decorators.cache import never_cache

from .models import Product,Cart

# DECORATOR 
def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Please Login First!!")
            return redirect('login')
    return inner



decs=[signin_required,never_cache]
# Create your views here.

# 1)SIGN IN
class SignInView(FormView):
    
    template_name="login.html"
    form_class=SignInForm

    def post(self,request,*args,**kwargs):
        form_ob=SignInForm(data=request.POST)
        if form_ob.is_valid():
            uname=form_ob.cleaned_data.get("username")
            pwd=form_ob.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                messages.success(request,"Login successfull...")
                return redirect('cust_home')
            else:
                messages.error(request,"Failed")
                return redirect('login')
        return render(request,"login.html",{"form_data":form_ob})
    

# 2) SIGN UP

# class SignUpView(View):
#     def get(self,request):
#         form_ob=SignUpForm()
#         return render(request,"signup.html",{"form_data":form_ob})
#     def post(self,request,*args,**kwargs):
#         form_ob=SignUpForm(data=request.POST)
#         if form_ob.is_valid():
#             form_ob.save()
#             messages.success(request,"Registration successfull...")
#             return redirect('login')
#         return render(request,"signup.html",{"form_data":form_ob})

class SignUpView(CreateView):
    form_class=SignUpForm
    template_name="signup.html"
    success_url=reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request,"Registration successfull")
        return super().form_valid(form)
    
   

# 3) LOG OUT
@method_decorator(decs,name="dispatch")
class LogOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('login')
    


