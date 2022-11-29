from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['identifiant', 'marque_modele', 'categorie','etat','affecte_a','noSerie','departement', 'date_affectation', 'date_achat', 'observation']