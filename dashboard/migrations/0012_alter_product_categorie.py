# Generated by Django 4.1.3 on 2022-12-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_alter_order_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categorie',
            field=models.CharField(blank=True, choices=[('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Onduleur', 'Onduleur'), ('Imprimante', 'Imprimante'), ('Serveur', 'Serveur'), ('Ecran', 'Ecran'), ('Nas', 'Nas'), ('Téléphonie', 'Téléphonie'), ('Accessoires', 'Accessoires'), ('Autre', 'Autre')], max_length=255, null=True),
        ),
    ]
