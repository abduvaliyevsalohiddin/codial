from django.contrib import admin

from .models import *


@admin.register(Soha)
class UstozAdmin(admin.ModelAdmin):
    list_display = ["id", "nom"]
    list_display_links = ["id", "nom"]
    search_fields = ["nom"]
    search_help_text = "Nom ustunlari bo'yicha qidiring"


@admin.register(Savollar)
class UstozAdmin(admin.ModelAdmin):
    list_display = ["id", "nom", "variat", "soha"]
    list_display_links = ["id", "nom"]
    search_fields = ["nom"]
    search_help_text = "Nom ustunlari bo'yicha qidiring"


# admin.site.register(Soha)
# admin.site.register(Savollar)
admin.site.register(UserProfile)
