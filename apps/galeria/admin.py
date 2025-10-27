from django.contrib import admin
from apps.galeria.models import Fotografia


class ListandoFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")
    list_filter = ("categoria", "usuario")
    list_per_page = 10
    list_editable = ("publicada",)

    search_fields = ("nome", "legenda")


admin.site.register(Fotografia, ListandoFotografia)
# Register your models here.
