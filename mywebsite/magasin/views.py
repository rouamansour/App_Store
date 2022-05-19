from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Produit
# Create your views here.
def index(request):
    template=loader.get_template('magasin/mesProduits.html')
    products= Produit.objects.all()
    return HttpResponse(template.render( { 'products':products} ))


