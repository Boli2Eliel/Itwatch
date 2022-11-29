# Generated by Django 4.1.3 on 2022-11-29 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifiant', models.CharField(blank=True, max_length=255, null=True)),
                ('categorie', models.CharField(blank=True, choices=[('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Onduleur', 'Onduleur'), ('Imprimante', 'Imprimante'), ('Serveur', 'Serveur'), ('Ecran', 'Ecran'), ('Nas', 'Nas'), ('Téléphonie', 'Téléphonie')], max_length=255, null=True)),
                ('etat', models.CharField(blank=True, choices=[('Bon(en service)', 'Bon(en service)'), ('Bon(pas en service)', 'Bon(pas en service)'), ('Hors service', 'Hors service'), ('En panne', 'En panne')], max_length=255, null=True)),
                ('departement', models.CharField(blank=True, choices=[('Administratif', 'Administratif'), ('Finance', 'Finance'), ('Indemnisation', 'Indemnisation'), ('Production', 'Production'), ('Informatique', 'Informatique'), ('Moyens généraux & logistique', 'Moyens généraux & logistique')], max_length=255, null=True)),
                ('affecte_a', models.CharField(blank=True, choices=[('MOUGNENGUE Florent', 'MOUGNENGUE Florent'), ('MOUTSOUKA Yvon', 'MOUTSOUKA Yvon'), ('MANTOT Marc', 'MANTOT Marc'), ('NZONGO Popaul', 'NZONGO Popaul'), ('NYATY God', 'NYATY God'), ('PEMOSSO Clozel', 'PEMOSSO Clozel'), ('TISSOKO Donald', 'TISSOKO Donald'), ('MITSINGOU Ibilakélé', 'MITSINGOU Ibilakélé'), ('MAKINA Van', 'MAKINA Van'), ('ETOUA Chadrack', 'ETOUA Chadrack'), ('NOMBO Grace', 'NOMBO Grace'), ('BOUKONGOU Emmanuel', 'BOUKONGOU Emmanuel'), ('KOUKA Didier', 'KOUKA Didier'), ('OMIERE David', 'OMIERE David'), ('EMMANUELLE De La Gloire', 'EMMANUELLE De La Gloire'), ('NGOUMA Cyrille', 'NGOUMA Cyrille')], max_length=255, null=True)),
                ('date_achat', models.DateField(blank=True, null=True)),
                ('prix_achat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('marque_modele', models.CharField(max_length=255, null=True)),
                ('noSerie', models.CharField(max_length=20, null=True, unique=True)),
                ('date_affectation', models.DateField(blank=True, null=True)),
                ('observation', models.TextField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Liste du matériel',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.PositiveIntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Order',
            },
        ),
    ]
