# Generated by Django 3.0.6 on 2020-05-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200505_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('entrees', 'entrees'), ('treats', 'treats'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
