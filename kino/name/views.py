from rest_framework import viewsets, permissions
from .models import Category, Director, Actor, Genre, Movie, Reviews
from .serializers import CategorySerializers, DirectorSerializers, ActorSerializers, GenreSerializers, MovieSerializers, ReviewsSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class ReviewsViewSets(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'email']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MovieViewSets(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']

class GenreViewSets(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']
class ActorViewSets(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers
    filter_backends = [DjangoFilterBackend]
#    filterset_fields = ['name']


class DirectorViewSets(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']
class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']