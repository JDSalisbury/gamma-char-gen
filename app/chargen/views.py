from chargen import serializers
from core import models
from rest_framework import viewsets, permissions


class SkillsViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.SkillsSerializer
    queryset = models.Skills.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OriginsViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.OriginsSerializer
    queryset = models.Origin.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class QuickCharViewSet(OriginsViewSet):
    queryset = models.Origin.objects.order_by('?')[:2]
