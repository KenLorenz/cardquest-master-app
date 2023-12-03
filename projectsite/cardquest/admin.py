from django.contrib import admin
from .models import PokemonCard, Trainer

# Register your models here.
# admin.site.register(PokemonCard)

@admin.register(PokemonCard)

@admin.register(Trainer)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity")
    search_fields = ("name",)