from django.contrib import admin
from .models import Origin, Character, Skills, OriginSecondary
from import_export.admin import ImportExportModelAdmin
from import_export import resources


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
admin.site.register(OriginSecondary, OriginSecondaryAdmin)


# Register your models here.
