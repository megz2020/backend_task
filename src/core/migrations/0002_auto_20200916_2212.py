# Generated by Django 3.0.5 on 2020-09-16 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeemachine',
            name='sku_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='code_machine', to='core.MachineCode'),
        ),
    ]
