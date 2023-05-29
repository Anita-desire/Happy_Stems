from django.shortcuts import render
from django.http import HttpResponse
from .forms import usersform
def home(request):
   context ={}
   form = usersform(request.POST or None, request.FILES or None)
   context['form']= form
   if form.is_valid():
        form.save()
        x=request.POST['name']
        y=request.POST['city']
     #  return render(request,"display.html",{'name':x,'city':y})
        return render(request,"index.html")
   else:
        return render(request, "home.html", context)
     
def about(request):
    return render(request,'about us.html')
 
def ShopNow(request):
    return render(request,'shopNow.html')
 
def shopNowsub(request):
    return render(request,'shopNowsub.html')
 
def Anniversary(request):
    return render(request,'Anniversary.html')
 
def loveNromance(request):
    return render(request,'loveNromance.html')

def feed1(request):
    return render(request,'feed1.html')
 
def login(request):
    return render(request,'login.html')
    
