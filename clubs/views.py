from django.shortcuts import render,redirect
from .models import Clubs

# Create your views here.

def home(request):
    clubs=Clubs.objects.all()
    context={'clubs':clubs}
    return render(request,'clubs/home.html',context)

def club(request,pk):
    clubs=Clubs.objects.get(id=pk)
    context={'clubs':clubs}
    return render(request,'clubs/club.html',context)

def createclub(request):
    if request.method=="POST":
        cname=request.POST['cname']
        description=request.POST['description']
        # print(cname,description)
        Clubs.objects.create(name=cname,description=description)
        return redirect('home')
    return render(request,'clubs/createclub.html')

def updateclub(request,pk):
    club=Clubs.objects.get(id=pk)
    context={'club':club}
    if request.method=="POST":
        cname=request.POST['cname']
        description=request.POST['description']
        Clubs.objects.filter(id=pk).update(name=cname,description=description)
        return redirect('home')
    return render(request,'clubs/updateroom.html',context)
