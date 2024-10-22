from django.shortcuts import render,redirect,HttpResponse
from .models import Clubs
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginpage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST['username'].lower()
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)


        except:
            messages.error(request,'user does not exist')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'username or password does not exist')


    context={'page':page}
    return render(request,'clubs/register.html',context)

def logoutuser(request):
    logout(request)
    return redirect('index')

def registeruser(request):
    # page='register'
    form=UserCreationForm()

    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'an error occured during registration')
    return render(request,'clubs/register.html',{'form':form})

def index(request):
    return render(request,'index.html')

def home(request):
    clubs=Clubs.objects.all()
    context={'clubs':clubs}
    return render(request,'clubs/home.html',context)

def club(request,pk):
    clubs=Clubs.objects.get(id=pk)
    context={'clubs':clubs}
    return render(request,'clubs/club.html',context)

@login_required(login_url='login')
def createclub(request):
    if request.method=="POST":
        cname=request.POST['cname']
        description=request.POST['description']
        # print(cname,description)
        Clubs.objects.create(name=cname,description=description,host_id=request.user.id)
        return redirect('home')
    return render(request,'clubs/createclub.html')

@login_required(login_url='login')
def updateclub(request,pk):
    club=Clubs.objects.get(id=pk)
    res=club.description
    # print(res)
    context={'club':club}
    
    if request.user != club.host:
        return HttpResponse("you are not allowed here!")
    if request.method=="POST":
        cname=request.POST['cname']
        description=request.POST['description']
        # print(type(description),len(description))
        if len(description)==0:
            description=res
        Clubs.objects.filter(id=pk).update(name=cname,description=description)
        return redirect('home')
    return render(request,'clubs/updateclub.html',context)

@login_required(login_url='login')
def deleteclub(request,pk):
    club=Clubs.objects.get(id=pk)
    if request.user != club.host:
        return HttpResponse("you are not allowed here!")
    if request.method=='POST':
        club.delete()
        return redirect('home')
    return render(request, 'clubs/deleteclub.html',{'obj':club})

