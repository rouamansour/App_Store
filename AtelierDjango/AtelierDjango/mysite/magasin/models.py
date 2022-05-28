from django.db import models
from datetime import date
# Create your models here.
class Produit(models.Model):
    TYPE_CHOICES=[('fr','Frais'),('cs','Conserve'),('em','emballé')]
    libelle=models.CharField(max_length=255)
    description=models.TextField()
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0.000)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True)    
    def __str__(self):
        return self.libelle+" "+self.description
        #associations avec les autres classes
    categorie= models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey('Fournisseur', on_delete=models.CASCADE,null=True)
    
class Categorie(models.Model):
    name= models.CharField(max_length=50,default="Alimentaire")

    @staticmethod
    def get_all_categories():
        return Categorie.objects.all()

    def __str__(self):
        return self.name 
class Fournisseur(models.Model):
    nom=models.CharField(max_length=255)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    
    def __str__(self):
        return self.nom+" "+self.adresse

class ProduitC(Produit):
    duree_garantie=models.IntegerField()
    def __str__(self):
        return "Produit consommable"+str(self.duree_garantie)

class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    def __str__(self):
        
        return str(self.dateCde)+"\n"+str(self.produits)+"\n Total: "+str(self.totalCde)
    from django.db import models

# Create your models here.
