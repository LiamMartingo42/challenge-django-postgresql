# Generated by Django 4.2.7 on 2023-11-21 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]