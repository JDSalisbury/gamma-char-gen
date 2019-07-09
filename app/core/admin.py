from django.contrib import admin
from .models import(
    Origin, Character, Skills, OriginSecondary, User,
    GammaCharacterSheet,
    Campaign,
    InventoryItem,
    Gear,
    Weapon,
)
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models
# Register your models here.


class UserAdmin(BaseUserAdmin):

    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser',)}
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


class OriginResource(resources.ModelResource):

    class Meta:
        model = Origin


class OriginAdmin(ImportExportModelAdmin):
    resource_class = OriginResource


class OriginSecondaryResource(resources.ModelResource):

    class Meta:
        model = OriginSecondary


class OriginSecondaryAdmin(ImportExportModelAdmin):
    resource_class = OriginSecondaryResource


admin.site.register(Origin, OriginAdmin)
admin.site.register(Character)
admin.site.register(Skills)
admin.site.register(Weapon)
admin.site.register(Gear)
admin.site.register(InventoryItem)
admin.site.register(Campaign)
admin.site.register(GammaCharacterSheet)
admin.site.register(OriginSecondary, OriginSecondaryAdmin)
admin.site.register(User, UserAdmin)

# Register your models here.
