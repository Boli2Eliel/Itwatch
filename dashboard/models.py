from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORIE =(
    ('Laptop', 'Laptop'),
    ('Desktop', 'Desktop'),
    ('Onduleur', 'Onduleur'),
    ('Imprimante', 'Imprimante'),
    ('Serveur', 'Serveur'),
    ('Ecran', 'Ecran'),
    ('Nas', 'Nas'),
    ('Téléphonie', 'Téléphonie'),
    ('Accessoires', 'Accessoires'),
    ('Autre', 'Autre'),
)
ETAT =(
    ('Bon(en service)', 'Bon(en service)'),
    ('Bon(pas en service)', 'Bon(pas en service)'),
    ('Hors service', 'Hors service'),
    ('En panne', 'En panne'),
)
DEPARTEMENT =(
    ('Administratif', 'Administratif'),
    ('Finance', 'Finance'),
    ('Indemnisation', 'Indemnisation'),
    ('Production', 'Production'),
    ('Informatique', 'Informatique'),
    ('Moyens généraux & logistique', 'Moyens généraux & logistique'),
)
UTILISATEUR =(
    ('MOUGNENGUE Florent', 'MOUGNENGUE Florent'),
    ('MOUTSOUKA Yvon', 'MOUTSOUKA Yvon'),
    ('MANTOT Marc', 'MANTOT Marc'),
    ('NZONGO Popaul', 'NZONGO Popaul'),
    ('NYATY God', 'NYATY God'),
    ('PEMOSSO Clozel', 'PEMOSSO Clozel'),
    ('TISSOKO Donald', 'TISSOKO Donald'),
    ('MITSINGOU Ibilakélé', 'MITSINGOU Ibilakélé'),
    ('MAKINA Van', 'MAKINA Van'),
    ('ETOUA Chadrack', 'ETOUA Chadrack'),
    ('NOMBO Grace', 'NOMBO Grace'),
    ('BOUKONGOU Emmanuel', 'BOUKONGOU Emmanuel'),
    ('KOUKA Didier', 'KOUKA Didier'),
    ('OMIERE David', 'OMIERE David'),
    ('EMMANUELLE De La Gloire', 'EMMANUELLE De La Gloire'),
    ('NGOUMA Cyrille', 'NGOUMA Cyrille'),
)

class Product(models.Model):
    identifiant = models.CharField(max_length=255, blank=True, null=True,)
    categorie = models.CharField(max_length=255, blank=True, null=True, choices=CATEGORIE)
    etat = models.CharField(max_length=255, blank=True, null=True, choices=ETAT)
    departement = models.CharField(max_length=255, blank=True, null=True, choices=DEPARTEMENT)
    affecte_a = models.CharField(max_length=255, blank=True, null=True, choices=UTILISATEUR)
    date_achat = models.DateField(blank=True, null=True)
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    marque_modele = models.CharField(max_length=255, null=True)
    noSerie = models.CharField(max_length=20, null=True, unique=True)
    date_affectation = models.DateField(blank=True, null=True)
    observation = models.TextField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Liste du matériel' # On change le nom de cette table dans l'Admin Panel

    def __str__(self):
        return f'{self.categorie}'

class Order(models.Model):
    product = models.CharField(max_length=255, blank=True, null=True,)
    category = models.CharField(max_length=255, blank=True, null=True, choices=CATEGORIE)
    staff = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True )

    class Meta:
        verbose_name_plural = 'Order'  # On change le nom de cette table dans l'Admin Panel

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'


