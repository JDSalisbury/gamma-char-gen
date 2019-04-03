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
        print(self.request.user.pk)
        serializer.save(user=self.request.user)


class QuickCharViewSet(OriginsViewSet):
    queryset = models.Origin.objects.order_by('?')[:2]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
