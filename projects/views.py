from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProjectForm, ReviewForm
from .models import Project,Review,Profile
from users.models import Message
from django.contrib import messages
from .utils import search,paginateProject
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
def projects(request):
    projects,search_query=search(request)
    projects,paginator,custom_range=paginateProject(request,projects)
    msg="hello you are on the projects page"
    contents={'message':msg , 'projects':projects, 'search_query':search_query,'paginator':paginator,'custom_range':custom_range}
    return render(request, "projects/projects.html",contents)
def project(request , pk):
    projectObj= Project.objects.get(id=pk)
    form=ReviewForm()
    reviewed=False
    tags=projectObj.tags.all()
    reviews=Review.objects.filter(project=projectObj)
    if request.method== "POST":
        form=ReviewForm(request.POST)
        review=form.save(commit=False)
        review.owner=request.user.profile
        review.project=projectObj
        review.save()
        projectObj.getVoteCount

        messages.success(request,"your review was successfully submited")
    context={'project':projectObj , 'tags':tags , "reviews":reviews,"form":form}
    return render(request, "projects/single_project.html",context)
@login_required(login_url='login')
def createProject(request):
    form=ProjectForm()
    profile=request.user.profile
    if (request.method == 'POST'):
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('projetcs')
    context={'form':form}
    return render(request, "projects/project_form.html",context)
@login_required(login_url='login')
def updateProject(request,pk):
    profile=request.user.profile
    project =profile.project_set.get(id=pk)
    form=ProjectForm(instance=project)
    if (request.method == 'POST'):
        form=ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projetcs')
    context={'form':form}
    return render(request, "projects/project_form.html",context)
@login_required(login_url='login')
def deleteProject(request,pk):
    profile=request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projetcs')
    context ={'object':project}
    return render(request, 'projects/delete_object.html' , context)
