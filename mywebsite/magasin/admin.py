from django.contrib import admin
from .models import Produit
from .models import Categorie
from .models import Fournisseur
from .models import ProduitC
from .models import Commande

admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Fournisseur)
admin.site.register(ProduitC) 
admin.site.register(Commande) 

# Register your models here.