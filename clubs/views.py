from django.shortcuts import render,redirect,HttpResponse
from .models import Clubs,Messages
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginpage(request):
    # page='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')

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


    # context={'page':page}
    return render(request,'clubs/login.html')

def logoutuser(request):
    logout(request)
    return redirect('index')

def registeruser(request):
    # page='register'
    # form=UserCreationForm()

    # if request.method=="POST":
    #     form=UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user=form.save(commit=False)
    #         user.username=user.username.lower()
    #         user.save()
    #         login(request,user)
    #         return redirect('home')

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if len(password)<7:
            messages.error(request,'password must be atleast 8 characters')
            return redirect('register')
        
        all_usernames=User.objects.filter(username=username)

        if all_usernames:
            messages.error(request,'username already exists, try another')
            return redirect('register')

        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,'user successfully created, login now!')
        
        return redirect('login')

    return render(request,'clubs/register.html')

def index(request):
    return render(request,'main.html')

def home(request):
    clubs=Clubs.objects.all()
    context={'clubs':clubs}
    return render(request,'clubs/home.html',context)

@login_required(login_url='login')
def club(request,pk):
    clubs=Clubs.objects.get(id=pk)
    all_messages=clubs.messages_set.all().order_by("-created_on")
    members=clubs.members.all()
    join=''
    leave=''
    comment=''
    if request.method=="POST":
        if 'join' in request.POST:
            join=request.POST['join']
            clubs.members.add(request.user)
        # print(join,type(join))

        if 'leave' in request.POST:
            leave=request.POST['leave']
            clubs.members.remove(request.user)
            # Messages.objects.filter(user=request.user,club_id=pk).delete()
        # print(leave,type(leave))

        if 'comment'in request.POST:
            if request.POST['comment']!='':
                c_messages=Messages.objects.create(
                user=request.user,
                club=clubs,
                body=request.POST.get('comment')
                )

        return redirect('club',pk=clubs.id)
    context={'clubs':clubs,'all_messages':all_messages,'members':members}
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

# def testing(request):
#     return render(request,'clubs/testing.html')