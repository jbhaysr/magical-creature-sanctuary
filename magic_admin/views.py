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
    # --- Add these lines for filtering, search, and ordering ---
    # For django-filter exact matches (e.g., ?field_name=value or ?owner__username=johndoe)
    filterset_fields = ['name', 'owner__username'] # Choose 1-2 relevant fields from your model
                                                    # For ForeignKeys, you can filter by related model fields like 'owner__username'

    # For SearchFilter (e.g., ?search=keyword)
    search_fields = ['name', 'species'] # Choose text-based fields from your model

    # For OrderingFilter (e.g., ?ordering=name or ?ordering=-creation_date)
    ordering_fields = ['name', 'id'] # Choose fields by which users can order results
    # ordering = ['-id'] # Optional: set a default ordering    
    # It will use DEFAULT_AUTHENTICATION_CLASSES and DEFAULT_PERMISSION_CLASSES from settings.py
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)    