# Generated by Django 3.1.3 on 2023-11-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='onlineuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alg_name', models.CharField(max_length=100)),
                ('sc1', models.FloatField()),
                ('sc2', models.FloatField()),
                ('sc3', models.FloatField()),
                ('sc4', models.FloatField()),
            ],
        ),
    ]