from rest_framework import serializers
from projects.models import Project,Tag,Review
from users.models import Profile
class Profileseializer(serializers.ModelSerializer):
     class Meta:
         model=Profile
         fields = "__all__"

class Tagseializer(serializers.ModelSerializer):
     class Meta:
         model=Tag
         fields = "__all__"

class Reviewseializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    owner=Profileseializer(many=False)
    tags=Tagseializer(many=True)
    reviews=serializers.SerializerMethodField()
    class Meta:
        model=Project
        fields = "__all__"
    def get_reviews(self,obj):
        reviews=obj.review_set.all()
        serializer =Reviewseializer(reviews,many=True)
        return serializer.data


