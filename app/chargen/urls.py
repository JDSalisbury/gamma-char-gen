from chargen import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('skill', views.SkillsViewSet)
router.register('origin', views.OriginsViewSet)

urlpatterns = [
] + router.urls
