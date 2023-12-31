"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cardquest.views import *
from cardquest import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.HomePageView.as_view(), name='home'),
        
        path('trainer_list', views.TrainerList.as_view(), name='trainer-list'),
        path('trainer_list/add', TrainerCreate.as_view(), name='trainer-add'),
        path('trainer_list/<pk>', TrainerUpdate.as_view(), name='trainer-update'),
        path('trainer_list/<pk>/delete', TrainerDelete.as_view(), name='trainer-delete'),
        
        path('pokemoncard_list', views.PokemonCardList.as_view(), name='pokemoncard-list'),
        path('pokemoncard_list/add', PokemonCardCreate.as_view(), name='pokemoncard-add'),
        path('pokemoncard_list/<pk>', PokemonCardUpdate.as_view(), name='pokemoncard-update'),
        path('pokemoncard_list/<pk>/delete', PokemonCardDelete.as_view(), name='pokemoncard-delete'),
        
        path('collection_list', views.CollectionList.as_view(), name='collection-list'),
        path('collection_list/add', views.CollectionCreate.as_view(), name='collection-add'),
        path('collection_list/<pk>', views.CollectionUpdate.as_view(), name='collection-update'),
        path('collection_list/<pk>/delete', views.CollectionDelete.as_view(), name='collection-delete'),
]
