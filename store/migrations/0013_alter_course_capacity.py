# Generated by Django 4.2.7 on 2024-11-30 14:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_oppositionuser_customer_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='capacity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
