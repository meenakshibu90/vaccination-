# Generated by Django 5.0.2 on 2024-03-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
