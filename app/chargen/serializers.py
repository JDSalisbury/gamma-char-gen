from rest_framework import serializers
from core.models import (
    Origin, Skills, Character,
    GammaCharacterSheet, InventoryItem,
    Gear, Weapon, Campaign
)


class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = "__all__"


class GearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gear
        fields = "__all__"


class WeaponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weapon
        fields = "__all__"


class InventoryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryItem
        fields = "__all__"


class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = "__all__"


class OriginsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Origin
        fields = (
            'id',
            'origin',
            'ability',
            'skill',
            'bonus',
            'ac',
            'fort',
            'ref',
            'will',
            'defense',
            'lvl_1',
            'lvl_2_or_6',
            'novice',
            'utility',
            'expert',
        )
        read_only_fields = ['id', ]


class CharacterSerializer(serializers.ModelSerializer):
    # random_skill = SkillsSerializer()

    class Meta:
        model = Character
        fields = '__all__'
        read_only_fields = ['id', ]


class GammaCharacterSheetSerializer(serializers.ModelSerializer):
    gear = GearSerializer(many=True, read_only=True,)
    weapons = WeaponSerializer(many=True, read_only=True,)
    inventory_items = InventoryItemSerializer(many=True, read_only=True,)
    campaign = CampaignSerializer(many=True, read_only=True,)

    class Meta:
        model = GammaCharacterSheet
        fields = '__all__'
        read_only_fields = ['id', ]
