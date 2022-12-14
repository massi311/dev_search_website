from django.forms import ModelForm
from .models import Project,Review
from users.models import Message
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model= Project
        fields= ['title','featured_image','description','demo_link','source_link','tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        for name,filed in self.fields.items():
            filed.widget.attrs.update({'class':'input'})
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
        labels={
            'value':"Place your vote",
            'body':"Add your comment with your vote"
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs.update({'class': 'input'})

