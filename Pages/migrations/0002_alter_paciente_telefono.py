# Generated by Django 5.1.7 on 2025-04-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
