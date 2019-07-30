from chargen import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('gear', views.GearViewSet)
router.register('campaign', views.CampaignViewSet)

router.register('weapon', views.WeaponViewSet)
router.register('inventoryitem', views.InventoryItemViewSet)
router.register('gammacharactersheet', views.GammaCharacterSheetViewSet)

router.register('addToInventory', views.AddToInventoryViewSet)

router.register('skill', views.SkillsViewSet)
router.register('origin', views.OriginsViewSet)
router.register('quickChar', views.QuickCharViewSet, base_name='quickChar')
router.register('character', views.CharacterViewSet)

urlpatterns = [
] + router.urls
