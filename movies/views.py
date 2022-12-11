from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer  # API用
from .models import Moviedata  # Moviedataモデル操作用
from django.views.generic import ListView,DetailView  # class based viewを使用するため　これはDjangoの標準機能


# Create your views here.
#API
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class = MovieSerializer


class ProductListView(ListView):
    model = Moviedata
    template_name = 'movies/index.html'
    context_object_name = 'Moviedata_OBJ'
    #paginate_by = 3