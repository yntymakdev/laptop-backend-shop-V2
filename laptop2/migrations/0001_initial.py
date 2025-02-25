# Generated by Django 5.1.1 on 2024-09-25 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('mac os ', 'mac OS'), ('dell', 'dell'), ('hp', 'hp'), ('lenovo', 'lenovo'), ('asus', 'asus')], max_length=32)),
                ('model', models.CharField(max_length=32)),
                ('processor', models.CharField(max_length=32)),
                ('ram_size', models.PositiveIntegerField(default=0)),
                ('storage_size', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LaptopPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/')),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='laptop2.laptop')),
            ],
        ),
    ]
