from chargen import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('skill', views.SkillsViewSet)
router.register('origin', views.OriginsViewSet)
router.register('quickChar', views.QuickCharViewSet, base_name='quickChar')

urlpatterns = [
] + router.urls
