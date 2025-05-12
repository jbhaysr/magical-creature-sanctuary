from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Creature

class CreatureListView(ListView):
    model = Creature

class CreatureDetailView(DetailView):
    model = Creature
