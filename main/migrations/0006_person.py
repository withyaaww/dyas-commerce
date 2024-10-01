# Generated by Django 5.1.1 on 2024-09-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('umur', models.IntegerField()),
                ('isHappy', models.BooleanField()),
            ],
        ),
    ]
