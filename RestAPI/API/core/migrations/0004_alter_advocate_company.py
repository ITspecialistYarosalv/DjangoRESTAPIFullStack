# Generated by Django 4.2.3 on 2023-07-13 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_advocate_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.companies'),
        ),
    ]
