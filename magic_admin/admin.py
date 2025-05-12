from django.contrib import admin
from .models import Creature, Habitat, Keeper

# Register your models here.
admin.site.register(Creature)
admin.site.register(Habitat)
admin.site.register(Keeper)