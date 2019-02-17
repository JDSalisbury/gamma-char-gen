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
    name = models.CharField(max_length=25)
    origin_primary = models.CharField(max_length=25)
    origin_secondary = models.CharField(max_length=25)
    ability_primary = models.CharField(max_length=5)
    ability_secondary = models.CharField(max_length=5)
    skill_primary = models.CharField(max_length=100)
    skill_secondary = models.CharField(max_length=100)
    random_skill = models.OneToOneField(to='Skills', on_delete='')
    bonus_primary = models.CharField(max_length=100)
    bonus_secondary = models.CharField(max_length=100)
    ac = models.IntegerField()
    fort = models.IntegerField()
    ref = models.IntegerField()
    will = models.IntegerField()
    defense_primary = models.TextField(max_length=1000)
    defense_secondary = models.TextField(max_length=1000)
    lvl_1_primary = models.TextField(max_length=1000)
    lvl_1_secondary = models.TextField(max_length=1000)
    lvl_2_or_6_primary = models.TextField(max_length=1000)
    lvl_2_or_6_secondary = models.TextField(max_length=1000)
    novice_primary = models.TextField(max_length=1000)
    novice_secondary = models.TextField(max_length=1000)
    utility_primary = models.TextField(max_length=1000)
    utility_secondary = models.TextField(max_length=1000)
    expert_primary = models.TextField(max_length=1000)
    expert_secondary = models.TextField(max_length=1000)


class Skills(models.Model):
    skill_name = models.CharField(max_length=25)
    key_ability = models.CharField(max_length=25)

    def __str__(self):
        return self.skill_name
