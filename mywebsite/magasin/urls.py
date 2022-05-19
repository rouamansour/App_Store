from xml.etree.ElementInclude import include
from django.urls import path,include
from django.contrib import admin
from . import views
from django.urls import path

# from django.conf.urls import url
urlpatterns=[
    path('',views.index),
    #path(r'^index/$', views.index, name='index'),
    #path('admin/',admin.site.urls),
    #path( r'^$', views.index , name='index') ,
    #path('produit/',views.produit),
    #path('categorie/',views.categorie),
]


