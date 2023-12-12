from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from cardquest.models import PokemonCard, Trainer, Collection
from django.shortcuts import render
from django.urls import reverse_lazy
from cardquest.forms import *
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
        
        # this doesn't work.. WHY??
        context['card_number_img'] = [x.card_number for x in context['pokemoncards']]
        context['card_number_main'] = [x.card_number for x in context['pokemoncards']]
        
        return context


# Trainer

class TrainerCreate(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'add.html' # url
    success_url = reverse_lazy('trainer-list') # name of urls

class TrainerUpdate(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'update.html'
    success_url = reverse_lazy('trainer-list')


class TrainerDelete(DeleteView):
    model = Trainer
    template_name = 'delete.html'
    url = reverse_lazy('trainer-delete')
    success_url = reverse_lazy('trainer-list')
    
# PokemonCards

class PokemonCardCreate(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'add.html' # url
    success_url = reverse_lazy('pokemoncard-list') # name of urls

class PokemonCardUpdate(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'update.html'
    success_url = reverse_lazy('pokemoncard-list')


class PokemonCardDelete(DeleteView):
    model = PokemonCard
    template_name = 'delete.html'
    url = reverse_lazy('trainer-delete')
    success_url = reverse_lazy('pokemoncard-list')