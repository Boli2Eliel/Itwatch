from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['identifiant', 'marque_modele', 'categorie','etat','affecte_a','noSerie','departement', 'date_affectation', 'date_achat', 'observation']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ['product', 'category', 'order_quantity', ]
        labels = {
            'product': 'Produit',
            'category': 'Categorie',
            'order_quantity': 'Quantité',
        }