# Generated by Django 5.0.2 on 2024-02-20 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impred', '0007_netmodels_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netmodels',
            name='accuracy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='netmodels',
            name='categories',
            field=models.IntegerField(),
        ),
    ]