from rest_framework import serializers
from .models import Category, Director, Actor, Genre, Movie, Reviews

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'description', 'age', 'image',]

class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'email', 'name', 'text', 'parent', 'movie', 'stars']