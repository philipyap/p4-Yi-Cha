# Generated by Django 3.1.1 on 2020-10-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20201001_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]