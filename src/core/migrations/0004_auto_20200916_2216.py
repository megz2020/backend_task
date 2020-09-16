# Generated by Django 3.0.5 on 2020-09-16 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_coffeemachine_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeemachine',
            name='pod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pod', to='core.CoffeePod'),
        ),
    ]
