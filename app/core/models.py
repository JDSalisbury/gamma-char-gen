from django.db import models
from rest_framework_tricks.models.fields import NestedProxyField


# Create your models here.


class Origin(models.Model):
    origin = models.CharField(max_length=25)
    ability = models.CharField(max_length=5)
    skill = models.CharField(max_length=100)
    bonus = models.CharField(max_length=100)
    ac = models.IntegerField()
    fort = models.IntegerField()
    ref = models.IntegerField()
    will = models.IntegerField()
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
    ac = models.IntegerField()
    fort = models.IntegerField()
    ref = models.IntegerField()
    will = models.IntegerField()
    defense = models.TextField(max_length=1000)
    lvl_1 = models.TextField(max_length=1000)
    lvl_2_or_6 = models.TextField(max_length=1000)
    novice = models.TextField(max_length=1000)
    utility = models.TextField(max_length=1000)
    expert = models.TextField(max_length=1000)

    def __str__(self):
        return self.origin


class Character(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    origin_primary = models.CharField(max_length=25, null=True, blank=True)
    origin_secondary = models.CharField(max_length=25, null=True, blank=True)
    ability_primary = models.CharField(max_length=5, null=True, blank=True)
    ability_secondary = models.CharField(max_length=5, null=True, blank=True)
    skill_primary = models.CharField(max_length=100, null=True, blank=True)
    skill_secondary = models.CharField(max_length=100, null=True, blank=True)
    random_skill = models.ForeignKey(
        to='Skills', on_delete=models.CASCADE, null=True, blank=True)
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


class Skills(models.Model):
    skill_name = models.CharField(max_length=25)
    key_ability = models.CharField(max_length=25)

    def __str__(self):
        return self.skill_name
