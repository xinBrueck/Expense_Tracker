# Generated by Django 2.2.4 on 2019-08-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20190803_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseitem',
            name='expenseDate',
            field=models.DateField(),
        ),
    ]