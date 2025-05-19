from django.db import models
from django.conf import settings

class Keeper(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100, null=True, blank=True)
    hire_date = models.DateField()
    contact_email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name}"

class Habitat(models.Model):
    name = models.CharField(max_length=100, unique=True)
    climate = models.CharField(max_length=100)
    magic_level = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class SpecialAbility(models.Model):
    ability_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.ability_name}"

class Creature(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    date_arrived = models.DateTimeField()
    temperament = models.CharField(max_length=100, null=True, blank=True)
    is_nocturnal = models.BooleanField(default=False)
    primary_keeper = models.ForeignKey(Keeper, on_delete=models.PROTECT)
    habitat = models.ForeignKey(Habitat, on_delete=models.PROTECT)
    special_abilities = models.ManyToManyField(SpecialAbility, through='CreatureAbility')

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_items' # Example: yourchosenmodel_items
    )

    def __str__(self):
        return f"{self.name}"

class CreatureAbility(models.Model):
    creature = models.ForeignKey(Creature, on_delete=models.CASCADE)
    special_ability = models.ForeignKey(SpecialAbility, on_delete=models.CASCADE)
    proficiency_level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.creature.name} {self.special_ability.name} {self.proficiency_level}"
