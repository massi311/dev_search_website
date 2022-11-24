from dataclasses import fields

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Skill,Message
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name','email','username','password1','password2'
        ]
        labels = {
            'first_name': "Name"
        }
    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        for name,filed in self.fields.items():
            filed.widget.attrs.update({'class':'input'})
class Profileform(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','location',
                  'bio','short_intro','profile_image',
                  'social_github','linkedin','social_twitter']

        def __init__(self, *args, **kwargs):
            super(Profileform, self).__init__(*args, **kwargs)
            for name, filed in self.fields.items():
                filed.widget.attrs.update({'class': 'input input--text'})
class Skillform(ModelForm):
    class Meta:
        model = Skill
        fields = ['name','description']
    def __init__(self, *args, **kwargs):
        super(Skillform, self).__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs.update({'class': 'input input--text'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [ 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs.update({'class': 'input'})


