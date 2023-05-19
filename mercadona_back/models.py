from django.db import models

# Create your models here.
class Catégorie(models.Model):
    libelle = models.CharField(max_length=250)
    def __str__(self):
        return self.libelle

class ImageProduit(models.Model):
    URL_Image_Produit = models.CharField(max_length=250)
    Nom_Image_Produit = models.CharField(max_length=250)
    def __str__(self):
        return self.Nom_Image_Produit
    
class Promotion(models.Model):
    Nom = models.CharField(max_length=50)
    Pourcentage = models.DecimalField(max_digits=10, decimal_places=2)
    Date_Début = models.DateField()
    Date_Fin = models.DateField()
    def __str__(self):
        return self.Nom

class Produit(models.Model):
    libelle = models.CharField(max_length=250)
    description = models.TextField
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    catégorie = models.ForeignKey(Catégorie , on_delete=models.CASCADE , null=False)
    image = models.ForeignKey(ImageProduit, on_delete=models.CASCADE , null=False)
    promotion = models.ManyToManyField(Promotion)
    def __str__(self):
        return self.libelle