import datetime
from django.test import TestCase
from mercadona_back.models import Catégorie
from mercadona_back.models import ImageProduit
from mercadona_back.models import Promotion
from mercadona_back.models import Produit

# Create your tests here.
class CategorieModelTest(TestCase):

    def test_string_representation(self):
        categ = Catégorie(libelle="Mon libelle")
        self.assertEqual(str(categ), categ.libelle)

class ImageModelTest(TestCase):

    def test_string_representation(self):
        image = ImageProduit(Nom_Image_Produit="Image")
        self.assertEqual(str(image), image.Nom_Image_Produit)

class PromotionModelTest(TestCase):

    def test_string_representation(self):
        promo = Promotion(Nom="Ma Promotion")
        self.assertEqual(str(promo), promo.Nom)

class ProduitModelTest(TestCase):

    def test_string_representation(self):
        produit = Produit(libelle="Mon produit")
        self.assertEqual(str(produit), produit.libelle)