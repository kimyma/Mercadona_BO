from django.contrib import admin
from mercadona_back.models import Produit, Promotion, Catégorie, ImageProduit

# Register your models here.

@admin.register (Promotion, Catégorie, ImageProduit)
class GenericAdmin(admin.ModelAdmin):
    pass

@admin.register (Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'prix' , 'catégorie')