from django.urls import path
from .views import *


urlpatterns = [
    path('', ReviewsViewSets.as_view({'get': 'list', 'post': 'create'}), name='reviews_list'),
    path('<int:pk>/', ReviewsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='name_detail'),
    path('actor/', ActorViewSets.as_view({'get': 'list', 'post': 'create'}), name='actor_list'),
    path('actor/<int:pk>/', ActorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='name_detail'),
    path('direct/', DirectorViewSets.as_view({'get': 'list', 'post': 'create'}), name='name_list'),
    path('direct/<int:pk>/', DirectorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='name_detail'),
    path('category/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}), name='name_list'),
    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='name_detail'),
]