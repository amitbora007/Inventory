from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import InData

# Create your views here.
def index(request):
 
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'welcome {username}')
            return redirect('/home',)
        else:
            messages.error(request, 'check your credentials', extra_tags='danger')
            return render(request, 'login.html')     
    return render(request,'login.html')

def lgout(request):
    logout(request)
    messages.success(request,'logout successful')
    return redirect('/')

def home(request):
    if request.user.is_anonymous:
        return redirect('/')

    username=request.user.username
    context = {"username": username}    
    return render(request, 'home.html', context)    

def stationary(request, option):
    if request.user.is_anonymous:
        return redirect('/')

    username=request.user.username
    
    data = InData.objects.filter(category='sta')
    if option=="Notebooks":
        context = {"choice": option, "data": data, "username": username} 
    elif option =="Writables":
        context  ={"choice":option, "data": data, "username": username}  
    else:
        context = {"choice": "Coming Soon", "data": data, "username": username}
    return render(request,'home.html',context)

def electronics(request, option):        
    if request.user.is_anonymous:
        return redirect('/')

    username=request.user.username
    data = InData.objects.filter(category='ele')
    if option =="Mobiles":
        context  ={"choice":option, "data": data, "username": username}  
    elif option =="Microwaves":
        context  ={"choice":option, "data": data, "username": username}
    elif option =="Laptops":
        context  ={"":option, "data": data, "username": username} 
    elif option =="Desktops":
        context  ={"choice":option, "data": data, "username": username}         
    else:
        context = {"choice": "Coming Soon", "data": data, "username": username}

    return render(request,'home.html',context)

def accessories(request, option):
    if request.user.is_anonymous:
        return redirect('/')

    username=request.user.username
    data = InData.objects.filter(category='acc')
    if option =="Mobile-Covers":
        context  ={"choice":option, "data": data, "username": username}
    elif option =="Earphones":
        context  ={"choice":option, "data": data, "username": username} 
    elif option =="Stickers":
        context  ={"choice":option, "data": data, "username": username}                  
    else:
        context = {"choice": "Coming Soon", "data": data, "username": username}

    return render(request,'home.html',context)
         
def about(request):
    if request.user.is_anonymous:
        return redirect('/')

    username=request.user.username
    context = {"username": username}
    return render(request, 'about.html', context)

def contact(request):
    if request.user.is_anonymous:
        return redirect('/')

    username=request.user.username    
    context = {"username": username}
    return render(request, 'contact.html', context)    

def add(request):
    if request.user.is_anonymous:
        return redirect('/')

    username=request.user.username
    context = {"username": username}
    if request.method =='POST':
        try:
            importedData = InData()
            importedData.category = request.POST.get('category')
            importedData.name = request.POST.get('name')
            importedData.priceperpiece = request.POST.get('price')
            importedData.qty = request.POST.get('qty')
            importedData.dname = request.POST.get('distributer')
            importedData.dloc = request.POST.get('location')
            importedData.totalprice = int(importedData.priceperpiece)*int(importedData.qty)
            importedData.save()
            messages.success(request,f'Added successfully to {importedData.category}.') 
        except:
            messages.error(request,'Failed, something went wrong.',extra_tags='danger') 
        return render(request, 'add.html', context)
    else:
        return render(request, 'add.html', context)

def delete(request, value):
    if request.user.is_anonymous:
        return redirect('/')

    username=request.user.username
    context = {"username": username}
    try:
        data = InData.objects.filter(name=value)
        data.delete()
        messages.success(request,'Deleted successfully.')  
    except:
        
        messages.error(request,'Failed, something went wrong.',extra_tags='danger')  
    return render(request, 'home.html', context)        