# Generated by Django 4.1.3 on 2022-11-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_order_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.CharField(blank=True, choices=[('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Onduleur', 'Onduleur'), ('Imprimante', 'Imprimante'), ('Serveur', 'Serveur'), ('Ecran', 'Ecran'), ('Nas', 'Nas'), ('Téléphonie', 'Téléphonie'), ('Accessoires', 'Accessoires'), ('Autre', 'Autre')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='categorie',
            field=models.CharField(blank=True, choices=[('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Onduleur', 'Onduleur'), ('Imprimante', 'Imprimante'), ('Serveur', 'Serveur'), ('Ecran', 'Ecran'), ('Nas', 'Nas'), ('Téléphonie', 'Téléphonie'), ('Accessoires', 'Accessoires'), ('Autre', 'Autre')], max_length=255, null=True),
        ),
    ]
