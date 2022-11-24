
from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.context_processors import request
from django.db.models import Q
from setuptools.command.install import install
from sqlparse import format
from .utils import search , paginateProject
from projects.views import projects
from .models import Profile,User,Skill,Message
from .forms import CustomUserCreationForm,Profileform,Skillform,MessageForm
# Create your views here.
def loginPage(request):
    page ="login"
    context= {
        'page':page
    }
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(message='username does not exist',request=request)
            return redirect('login')
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(message='username or password is incorrect', request=request)
            return redirect('login')

    return render(request, 'users/login-register.html',context)
def logoutUser(request):
    logout(request)
    messages.error(message='user was successfully logged out', request=request)
    return redirect('login')
def registerUser(request):
    form =CustomUserCreationForm()
    page='register'
    context={
        'page':page,
        'form':form,
    }
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "user account was created!")
            login(request,user)
            return redirect('edit-account')
        else:
            messages.error(request, "an error has occurred during registration")


    return render(request,'users/login-register.html',context)

def profiles(request):
    profiles,search_query=search(request)
    profiles, paginator, custom_range = paginateProject(request, profiles)
    context={'profiles':profiles,"search_query":search_query,"paginator":paginator,"custom_range":custom_range}
    return render(request,'users/profiles.html',context)
def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    topSkills= profile.skill_set.exclude(description__exact="")
    otherSkills=profile.skill_set.filter(description="")
    context={
        'profile': profile,
        'topSkills':topSkills,
        'otherSkills':otherSkills,

    }
    return render(request,'users/user-profile.html',context)
@login_required(login_url="login")
def userAccount(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    skills=profile.skill_set.all()
    projects=profile.project_set.all()
    context={
        'profile':profile,
        'skills':skills,
        'projects':projects,

    }
    return render(request,'users/account.html', context)

@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile
    form=Profileform(instance=profile)

    if request.method == "POST":
        form = Profileform(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')


    context={
        'form':form,
        'profile':profile
    }
    return render(request,'users/profile-form.html',context)
@login_required(login_url='login')
def createSkill(request):
    profile=request.user.profile
    form = Skillform()
    context={
        'form':form,
        'page':'create',
    }
    if request.method == 'POST':
        form = Skillform(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.owner=profile
            form.save()
            return redirect("account")

    return render(request,"users/skill_form.html",context)
@login_required(login_url='login')
def updateSkill(request,pk):
    skill=Skill.objects.get(id=pk)
    form=Skillform(instance=skill)
    context={
        'form':form,
        'page':'update',
    }
    if request.method == 'POST':
        form = Skillform(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            return redirect("account")
    return render(request, 'users/skill_form.html', context)

@login_required(login_url='login')
def deleteskill(request,pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    skill.delete()
    return redirect("account")
@login_required(login_url='login')
def inbox(request):
    message=Message.objects.filter(recipient=request.user.profile)
    #profile=request.user.profile
    #message=profile.messages.all()
    unread_count=message.filter(is_read=False).count()
    context={'message':message,"unread_count":unread_count }
    return render(request,"users/inbox.html",context)
@login_required(login_url="login")
def viewMessage(request,pk):
    profile=request.user.profile
    message=profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read=True
        message.save()
    context={"message":message}
    return render(request,"users/message.html",context)


@login_required(login_url='login')
def sendMessage(request, pk):
    form = MessageForm()
    message = ""
    profile = request.user.profile
    recipient = Profile.objects.get(id=pk)
    context = {"form": form}

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = profile
            message.name= profile.name
            message.recipient = recipient
            message.save()
    return render(request, "users/send_form.html", context)

def about_me(request):

    return render(request,"about-me.html")