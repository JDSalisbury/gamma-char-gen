# from rest_framework_tricks.models.fields import NestedProxyField
import os
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(null=True, default=True)
    is_staff = models.BooleanField(null=True, default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Origin(models.Model):
    origin = models.CharField(max_length=25)
    ability = models.CharField(max_length=5)
    skill = models.CharField(max_length=100)
    bonus = models.CharField(max_length=100)
    ac = models.IntegerField(null=True, default=0)
    fort = models.IntegerField(null=True, default=0)
    ref = models.IntegerField(null=True, default=0)
    will = models.IntegerField(null=True, default=0)
    defense = models.TextField(max_length=1000)
    lvl_1 = models.TextField(max_length=1000)
    lvl_2_or_6 = models.TextField(max_length=1000)
    novice = models.TextField(max_length=1000)
    utility = models.TextField(max_length=1000)
    expert = models.TextField(max_length=1000)

    def __str__(self):
        return self.origin


class OriginSecondary(models.Model):
    origin = models.CharField(max_length=25)
    ability = models.CharField(max_length=5)
    skill = models.CharField(max_length=100)
    bonus = models.CharField(max_length=100)
    ac = models.IntegerField(null=True, default=0)
    fort = models.IntegerField(null=True, default=0)
    ref = models.IntegerField(null=True, default=0)
    will = models.IntegerField(null=True, default=0)
    defense = models.TextField(max_length=1000)
    lvl_1 = models.TextField(max_length=1000)
    lvl_2_or_6 = models.TextField(max_length=1000)
    novice = models.TextField(max_length=1000)
    utility = models.TextField(max_length=1000)
    expert = models.TextField(max_length=1000)

    def __str__(self):
        return self.origin


class Character(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=25, null=True, blank=True)
    origin_primary = models.CharField(max_length=25, null=True, blank=True)
    origin_secondary = models.CharField(max_length=25, null=True, blank=True)
    ability_primary = models.CharField(max_length=5, null=True, blank=True)
    ability_secondary = models.CharField(max_length=5, null=True, blank=True)
    skill_primary = models.CharField(max_length=100, null=True, blank=True)
    skill_secondary = models.CharField(max_length=100, null=True, blank=True)
    random_skill = models.CharField(max_length=100, null=True, blank=True)
    bonus_primary = models.CharField(max_length=100, null=True, blank=True)
    bonus_secondary = models.CharField(max_length=100, null=True, blank=True)
    ac = models.IntegerField(null=True, blank=True)
    fort = models.IntegerField(null=True, blank=True)
    ref = models.IntegerField(null=True, blank=True)
    will = models.IntegerField(null=True, blank=True)
    defense_primary = models.TextField(max_length=1000, null=True, blank=True)
    defense_secondary = models.TextField(
        max_length=1000, null=True, blank=True)
    lvl_1_primary = models.TextField(max_length=1000, null=True, blank=True)
    lvl_1_secondary = models.TextField(max_length=1000, null=True, blank=True)
    lvl_2_or_6_primary = models.TextField(
        max_length=1000, null=True, blank=True)
    lvl_2_or_6_secondary = models.TextField(
        max_length=1000, null=True, blank=True)
    novice_primary = models.TextField(max_length=1000, null=True, blank=True)
    novice_secondary = models.TextField(max_length=1000, null=True, blank=True)
    utility_primary = models.TextField(max_length=1000, null=True, blank=True)
    utility_secondary = models.TextField(
        max_length=1000, null=True, blank=True)
    expert_primary = models.TextField(max_length=1000, null=True, blank=True)
    expert_secondary = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class Skills(models.Model):
    skill_name = models.CharField(max_length=25)
    key_ability = models.CharField(max_length=25)

    def __str__(self):
        return self.skill_name


class GammaCharacterSheet(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )   # Placed on Create

    # A Choice after Character Creation
    image = models.CharField(max_length=255, blank=True, null=True)
    archived = models.BooleanField(
        null=True, default=False)  # In place of delete
    temp = models.CharField(max_length=255, blank=True, null=True)

    # Auto Generated then editable
    name = models.CharField(max_length=255, blank=True, null=True)
    lvl = models.IntegerField(null=True, default=1)  # Auto generated
    origin1_first = models.CharField(
        max_length=255, blank=True, null=True)  # Placed
    origin2_second = models.CharField(
        max_length=255, blank=True, null=True)  # Placed

    strength = models.IntegerField(null=True, default=0)  # Set
    dexterity = models.IntegerField(null=True, default=0)  # Set
    wisdom = models.IntegerField(null=True, default=0)  # Set
    constitution = models.IntegerField(null=True, default=0)  # Set
    intelligence = models.IntegerField(null=True, default=0)  # Set
    charisma = models.IntegerField(null=True, default=0)  # Set

    skill1 = models.CharField(max_length=255, blank=True, null=True)  # Set
    skill2 = models.CharField(max_length=255, blank=True, null=True)  # Set
    skill3 = models.CharField(max_length=255, blank=True, null=True)  # Set
    skill1_mod = models.IntegerField(null=True, default=0)  # Set
    skill2_mod = models.IntegerField(null=True, default=0)  # Set
    skill3_mod = models.IntegerField(null=True, default=0)  # Set
    hp = models.IntegerField(null=True, default=0)  # Set
    speed = models.IntegerField(null=True, default=6)
    ac = models.IntegerField(null=True, default=0)
    fort = models.IntegerField(null=True, default=0)  # Set
    ref = models.IntegerField(null=True, default=0)  # Set
    will = models.IntegerField(null=True, default=0)  # Set

    overcharge_bonus1 = models.CharField(
        max_length=255, blank=True, null=True)  # Set
    overcharge_bonus2 = models.CharField(
        max_length=255, blank=True, null=True)  # Set

    defense1 = models.CharField(max_length=255, blank=True, null=True)  # Sent
    defense2 = models.CharField(max_length=255, blank=True, null=True)  # Sent
    defense_ability1 = models.CharField(
        max_length=9255, blank=True, null=True)  # Sent
    defense_ability2 = models.CharField(
        max_length=9255, blank=True, null=True)  # Sent

    critical_choice_lvl_2 = models.CharField(
        max_length=2955, blank=True, null=True)
    critical_choice_lvl_6 = models.CharField(
        max_length=2955, blank=True, null=True)

    critical1 = models.CharField(
        max_length=2955, blank=True, null=True)  # Sent
    critical2 = models.CharField(
        max_length=2955, blank=True, null=True)  # Sent

    novice_1 = models.CharField(max_length=9255, blank=True, null=True)  # Set
    novice_2 = models.CharField(max_length=9255, blank=True, null=True)  # Set

    utility_choice_lvl_3 = models.CharField(
        max_length=9255, blank=True, null=True)
    utility_choice_lvl_7 = models.CharField(
        max_length=9255, blank=True, null=True)

    utility_1 = models.CharField(
        max_length=9255, blank=True, null=True)  # Sent
    utility_2 = models.CharField(
        max_length=9255, blank=True, null=True)  # Sent

    expert_choice_lvl_5 = models.CharField(
        max_length=9255, blank=True, null=True)
    expert_choice_lvl_9 = models.CharField(
        max_length=9255, blank=True, null=True)

    expert_1 = models.CharField(max_length=9255, blank=True, null=True)  # Sent
    expert_2 = models.CharField(max_length=9255, blank=True, null=True)  # Sent

    campaign = models.ManyToManyField('Campaign')

    def __str__(self):
        return self.name


class Gear(models.Model):
    gammaCharacterSheet = models.ForeignKey(
        "core.GammaCharacterSheet", on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="gear")
    name = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    ac_bonus = models.IntegerField(null=True, default=0)
    equipped = models.BooleanField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    gammaCharacterSheet = models.ForeignKey(
        "core.GammaCharacterSheet", on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="inventory_items")
    name = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    cost = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    gammaCharacterSheet = models.ForeignKey(
        "core.GammaCharacterSheet", on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="weapons")
    name = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    dice = models.CharField(max_length=255, blank=True, null=True)
    bonus = models.IntegerField(null=True, default=0)
    accuracy = models.IntegerField(null=True, default=0)
    ability_modifier = models.CharField(max_length=255, blank=True, null=True)
    equipped = models.BooleanField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
