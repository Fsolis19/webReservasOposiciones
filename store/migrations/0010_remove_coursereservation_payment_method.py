# Generated by Django 4.2.7 on 2024-11-28 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_course_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursereservation',
            name='payment_method',
        ),
    ]
