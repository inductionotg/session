from django.shortcuts import render
from testApp.forms import *

# Create your views here.
def add_item_view(request):
    form=Add_item_form()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
    return render(request,'testApp/additem.html',{'form':form})
def display_item_view(request):
    return render(request,'testApp/display.html')
