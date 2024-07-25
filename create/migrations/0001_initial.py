# Generated by Django 5.0.6 on 2024-07-06 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ful_name', models.CharField(max_length=50)),
                ('emo_code', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=15)),
                ('postion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create.postion')),
            ],
        ),
    ]
