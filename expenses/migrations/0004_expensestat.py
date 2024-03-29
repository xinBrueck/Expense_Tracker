# Generated by Django 2.2.4 on 2019-08-03 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_auto_20190803_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalBudget', models.DecimalField(decimal_places=2, max_digits=5)),
                ('totalExpense', models.DecimalField(decimal_places=2, max_digits=5)),
                ('totalLeft', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
