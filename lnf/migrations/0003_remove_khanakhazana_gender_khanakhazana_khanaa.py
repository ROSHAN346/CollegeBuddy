# Generated by Django 5.2 on 2025-04-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lnf', '0002_alter_khanakhazana_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='khanakhazana',
            name='gender',
        ),
        migrations.AddField(
            model_name='khanakhazana',
            name='khanaa',
            field=models.CharField(choices=[('B', 'Beverage'), ('S', 'Snack'), ('D', 'Desert')], default='food', max_length=2),
        ),
    ]
