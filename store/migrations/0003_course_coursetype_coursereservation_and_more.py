# Generated by Django 4.2.7 on 2024-11-15 11:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_brand_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('city', models.CharField(max_length=200)),
                ('is_available', models.BooleanField(default=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Course type',
                'verbose_name_plural': 'Course types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CourseReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateTimeField(auto_now_add=True)),
                ('reserved_on', models.DateTimeField()),
                ('is_confirmed', models.BooleanField(default=False)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.course')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer')),
            ],
            options={
                'verbose_name': 'Course reservation',
                'verbose_name_plural': 'Course reservations',
                'ordering': ['-reservation_date'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.coursetype'),
        ),
    ]