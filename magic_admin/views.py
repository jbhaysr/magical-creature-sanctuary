from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from .models import Creature
from .serializers import CreatureSerializer

class CreatureListView(ListView):
    model = Creature

class CreatureDetailView(LoginRequiredMixin, DetailView):
    model = Creature

class CreatureViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing instances of YourChosenModel.
    Provides `list` and `retrieve` actions.
    """
    queryset = Creature.objects.all() # The collection of all objects for this model
    serializer_class = CreatureSerializer
    # It will use DEFAULT_AUTHENTICATION_CLASSES and DEFAULT_PERMISSION_CLASSES from settings.py