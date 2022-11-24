from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('',views.profiles, name="profiles"),
    path('profile/<str:pk>',views.userProfile,name="user-profile"),
    path('login/', views.loginPage,name='login'),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),
    path('account/',views.userAccount,name='account'),
    path('edit-account',views.editAccount,name="edit-account"),
    path('create-skill',views.createSkill,name='create-skill'),
    path('update-skill/<str:pk>',views.updateSkill,name='update-skill'),
    path('delete-skill/<str:pk>',views.deleteskill,name='delete-skill'),
    path('inbox',views.inbox,name="inbox"),
    path('message/<str:pk>',views.viewMessage,name='view_message'),
    path('send-form/<str:pk>', views.sendMessage, name="send-form"),


]