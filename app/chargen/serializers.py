from rest_framework import serializers
from core.models import Origin, Skills, Character


class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = (
            'id',
        )


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
