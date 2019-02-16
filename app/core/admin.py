from django.contrib import admin
from .models import Origin, Character, Skills
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class OriginResource(resources.ModelResource):

    class Meta:
        model = Origin


class OriginAdmin(ImportExportModelAdmin):
    resource_class = OriginResource


admin.site.register(Origin, OriginAdmin)
admin.site.register(Character)
admin.site.register(Skills)

# Register your models here.
