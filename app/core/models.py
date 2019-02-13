from django.db import models

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
