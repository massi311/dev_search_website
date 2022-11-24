from .models import User,Profile
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete
def createProfile(sender,instance, created, **kwargs):

    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
    subject="welcome to this site"
    body="we are glad you are here"
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [instance.email],
        fail_silently=False
    )
def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created == False:
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()
def deleteProfile(sender,instance, **kwargs):
    user=instance.user
    user.delete()
post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteProfile,sender=Profile)