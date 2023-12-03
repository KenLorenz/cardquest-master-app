from django.contrib import admin
from .models import PokemonCard, Trainer, Collection

# Register your models here.
# admin.site.register(PokemonCard)

# add admin menus

@admin.register(Collection)

@admin.register(PokemonCard)

@admin.register(Trainer)

class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name")
    search_fields = ("name",)
