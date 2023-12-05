from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Trainer, Collection
from django.shortcuts import render
# Create your views here.

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 15
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncards'
    template_name = "pokemoncards.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['card_number_format'] = [f"{card.card_number:03d}" for card in context['pokemoncards']]
        
        return context

