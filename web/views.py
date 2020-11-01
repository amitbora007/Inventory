from django.shortcuts import render
from .models import InData

# Create your views here.
def index(request):
    return render(request,'home.html')

def stationary(request, option):
    data = InData.objects.filter(category='sta')
    if option=="Notebooks":
        context = {"choice": option, "data": data} 
    elif option =="Writables":
        context  ={"choice":option, "data": data}  
    else:
        context = {"choice": "Coming Soon", "data": data}
    return render(request,'home.html',context)

def electronics(request, option):        
    data = InData.objects.filter(category='ele')
    if option =="Mobiles":
        context  ={"choice":option, "data": data}  
    elif option =="Microwaves":
        context  ={"choice":option, "data": data}
    elif option =="Laptops":
        context  ={"":option, "data": data} 
    elif option =="Desktops":
        context  ={"choice":option, "data": data}         
    else:
        context = {"choice": "Coming Soon", "data": data}

    return render(request,'home.html',context)

def accessories(request, option):
    data = InData.objects.filter(cat='acc')
    if option =="Mobile-Covers":
        context  ={"choice":option, "data": data}
    elif option =="Earphones":
        context  ={"choice":option, "data": data} 
    elif option =="Stickers":
        context  ={"choice":option, "data": data}                  
    else:
        context = {"choice": "Coming Soon", "data": data}

    return render(request,'home.html',context)
         
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')    

def add(request):
    if request.method =='POST':
        importedData = InData()
        importedData.category = request.POST.get('category')
        importedData.name = request.POST.get('name')
        importedData.priceperpiece = request.POST.get('price')
        importedData.qty = request.POST.get('qty')
        importedData.dname = request.POST.get('distributer')
        importedData.dloc = request.POST.get('location')
        importedData.totalprice = int(importedData.priceperpiece)*int(importedData.qty)
        importedData.save()
        return render(request, 'add.html')
    else:
        return render(request, 'add.html')

def delete(request, value):
    data = InData.objects.get(name=value)
    data.delete()
    return render(request, 'home.html')        