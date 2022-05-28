from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Produit

def index(request):
    template=loader.get_template('magasin/search.html')
    products=Produit.objects.all()
    return HttpResponse(template.render( { 'products':products} ))
def list(request):
    template=loader.get_template('magasin/search.html')
    products=Produit.objects.all()
    return HttpResponse(template.render( { 'products':products} ))
# Create your views here.
