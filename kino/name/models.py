from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField
    description = models.TextField()
    image = models.ImageField(upload_to='actor/')

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=32)
    tagline = models.CharField(max_length=32)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    year = models.IntegerField()
    country = models.CharField(max_length=32)
    directors = models.ManyToManyField(Director, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    world_premiere = models.DateField()
    budget = models.BigIntegerField()
    fees_in_usa = models.BigIntegerField()
    fess_in_world = models.BigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=32)
    text = models.TextField()
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField()

    def __str__(self):
        return self.name
