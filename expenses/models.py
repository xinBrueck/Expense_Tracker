from django.db import models

class ExpenseItem(models.Model):
    EXPENSE_CATEGORY_CHOICES = [
        ('Utilities', 'Utilities'),
        ('Health Care', 'Health Care'),
        ('Grocery/Restaurant', 'Grocery/Restaurant'),
        ('Personal Care', 'Personal Care'),
        ('Entertainment', 'Entertainment'),
        ('Membership Fees', 'Membership Fees'),
        ('Transportation', 'Transportation'),
        ('Education', 'Education'),
        ('Other', 'Other'),
    ]

    expenseName = models.TextField()
    expenseAmt = models.DecimalField(max_digits=8, decimal_places=2)
    expenseCategory = models.CharField(
        max_length=25,
        choices=EXPENSE_CATEGORY_CHOICES,
    )
    expenseDate = models.DateField()

class ExpenseStat(models.Model):
    totalBudget = models.DecimalField(max_digits = 8, decimal_places = 2)
    totalExpense = models.DecimalField(max_digits = 8, decimal_places = 2)
    totalLeft = models.DecimalField(max_digits = 8, decimal_places = 2)
