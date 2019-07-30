from chargen import serializers
from core import models
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import ensure_csrf_cookie


class SkillsViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.SkillsSerializer
    queryset = models.Skills.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OriginsViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.OriginsSerializer
    queryset = models.Origin.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CharacterSerializer
    queryset = models.Character.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def perform_destroy(self, serializer):
    #     serializer.delete(user=self.request.user)


class GammaCharacterSheetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GammaCharacterSheetSerializer
    queryset = models.GammaCharacterSheet.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WeaponViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.WeaponSerializer
    queryset = models.Weapon.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class InventoryItemViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.InventoryItemSerializer
    queryset = models.InventoryItem.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GearViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.GearSerializer
    queryset = models.Gear.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CampaignViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.CampaignSerializer
    queryset = models.Campaign.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class QuickCharViewSet(OriginsViewSet):
    queryset = models.Origin.objects.order_by('?')[:2]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AddToInventoryViewSet(InventoryItemViewSet):

    def perform_create(self, serializer):
        item = serializer.save()
        item.user.add()
