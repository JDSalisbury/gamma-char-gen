from django.contrib import admin
from .models import Origin
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class OriginResource(resources.ModelResource):

    class Meta:
        model = Origin


class OriginAdmin(ImportExportModelAdmin):
    resource_class = OriginResource


admin.site.register(Origin, OriginAdmin)


# Register your models here.
