from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografia(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')
    list_display_links = ('id', 'nome')
    search_fields = ("nome","legenda")

admin.site.register(Fotografia, ListandoFotografia)
# Register your models here.
