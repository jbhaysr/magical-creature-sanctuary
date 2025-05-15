from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from .models import Creature

class CreatureListView(ListView):
    model = Creature

class CreatureDetailView(LoginRequiredMixin, DetailView):
    model = Creature
