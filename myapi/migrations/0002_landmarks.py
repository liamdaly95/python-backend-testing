# Generated by Django 5.0 on 2023-12-21 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landmark', models.CharField(max_length=60)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.locations')),
            ],
        ),
    ]
