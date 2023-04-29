from django.contrib import admin
from mercadona_back.models import Produit, Promotion, Catégorie, ImageProduit

# Register your models here.

@admin.register (Produit, Promotion, Catégorie, ImageProduit)
class GenericAdmin(admin.ModelAdmin):
    pass