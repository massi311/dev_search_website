from django.db.models import Q
from .models import Skill,Profile
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def paginateProject(request,projects):
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(projects, results)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 2)
    if (rightIndex > paginator.num_pages):
        rightIndex = paginator.num_pages + 1
    custom_range = range(leftIndex, rightIndex)
    return (projects,paginator,custom_range)
def search(request):
    skills=''
    search_query=''

    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
        skills=Skill.objects.filter(name__icontains=search_query)

    profiles=Profile.objects.distinct().filter(Q(name__icontains=search_query)|
                                    Q(short_intro__icontains=search_query)|
                                    Q(skill__in=skills))
    return profiles,search_query