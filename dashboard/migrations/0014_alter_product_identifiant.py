# Generated by Django 4.1.3 on 2022-12-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_product_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='identifiant',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]