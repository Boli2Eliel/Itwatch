# Generated by Django 4.1.3 on 2022-11-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.CharField(blank=True, choices=[('ordinateur', 'Ordinateur'), ('écran', 'écran'), ('accessoires', 'accessoires'), ('autres', 'autres')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='categorie',
            field=models.CharField(blank=True, choices=[('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Onduleur', 'Onduleur'), ('Imprimante', 'Imprimante'), ('Serveur', 'Serveur'), ('Ecran', 'Ecran'), ('Nas', 'Nas'), ('Téléphonie', 'Téléphonie'), ('autres', 'autres')], max_length=255, null=True),
        ),
    ]