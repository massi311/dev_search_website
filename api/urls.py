from django.urls import path

from api import views

urlpatterns = [
    path("",views.getRoutes),
    path("projects/",views.getProjects),
    path("projects/<str:id>",views.getProject),
    path("projects/<str:id>/vote",views.getProject),
]