# Generated by Django 2.2.4 on 2019-08-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseitem',
            name='expenseCategory',
            field=models.CharField(choices=[('Utilities', 'Utilities'), ('Health Care', 'Health Care'), ('Grocery/Restaurant', 'Grocery/Restaurant'), ('Personal Care', 'Personal Care'), ('Entertainment', 'Entertainment'), ('Membership Fees', 'Membership Fees'), ('Transportation', 'Transportation'), ('Education', 'Education'), ('Other', 'Other')], max_length=25),
        ),
    ]
