# Generated by Django 5.0 on 2024-01-17 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]