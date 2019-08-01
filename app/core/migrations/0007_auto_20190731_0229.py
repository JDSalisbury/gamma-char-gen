# Generated by Django 2.1.5 on 2019-07-31 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_gammacharactersheet_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='gammaCharacterSheet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventory_items', to='core.GammaCharacterSheet'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='gammaCharacterSheet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weapons', to='core.GammaCharacterSheet'),
        ),
    ]