from rest_framework import serializers
from core.models import Movie, Rating
from django.contrib.auth.models import User

class  UserSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class MovieSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_ratings')


class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = '__all__'
