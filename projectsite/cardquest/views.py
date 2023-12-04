from django.views.generic.list import ListView
from django.shortcuts import render
from cardquest.models import PokemonCard, Trainer, Collection

# Create your views here.

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'templates/collection.html'
class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'templates/trainers.html'
    paginate_by = 15
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "templates/base.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
