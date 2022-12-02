from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


admin.site.site_header = "IT'WATCH Dashboard" #changer le titre de l'Admin Panel

class ProductAdmin(admin.ModelAdmin):
    list_display = ('identifiant', 'marque_modele', 'categorie','etat','affecte_a','noSerie', 'date_affectation', 'date_achat', 'created_at','updated_at')
    list_filter = ('categorie', 'marque_modele','etat')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Category, CategoryAdmin)

