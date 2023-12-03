from django.contrib import admin
from .models import PokemonCard, Trainer, Collection

# Register your models here.
# admin.site.register(PokemonCard)

# add admin menus

@admin.register(Collection)

@admin.register(PokemonCard)

@admin.register(Trainer)

class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity")
    search_fields = ("name",)

class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate")
    search_fields = ("name",)
    
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("card", "collection_date")
    search_fields = ("name",)