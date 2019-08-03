from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ExpenseItem, ExpenseStat
from datetime import datetime

def expensesView(request):
    expenseItems = ExpenseItem.objects.all()

    ##filter by this month
    today = datetime.today()
    currentYear = today.year
    currentMonth = today.month

    expenseItems = expenseItems.filter(expenseDate__year=currentYear,
                                expenseDate__month=currentMonth).order_by('expenseDate')

    ##calculate total expense
    totalExpense = 0
    for expense in expenseItems:
        totalExpense += float(expense.expenseAmt)

    totalLeft = 3000 - totalExpense

    # return render(request, "stats.html", {'expenses': expenseItems,'stats':expenseStat})
    return render(request, "stats.html", {'expenses': expenseItems,
                                          'totalExpense':totalExpense,
                                          'totalLeft':totalLeft})



def addExpenses(request):
    name = request.POST['expense']
    amt = request.POST['expenseAmount']
    category = request.POST['expenseCategory']
    date = request.POST['expenseDate']

    new_expense = ExpenseItem(expenseName = name,
                            expenseAmt = amt,
                            expenseCategory = category,
                            expenseDate = date)

    new_expense.save()

    return HttpResponseRedirect('/')

def deleteExpenses(request, expense_id):
    expense_to_delete = ExpenseItem.objects.get(id = expense_id)
    expense_to_delete.delete()

    return HttpResponseRedirect('/')


# def addBudget(request):
#     budget = float(request.POST.get('totalBudget'))
#     print(budget)
#
#     expenseItems = ExpenseItem.objects.all()
#
#     ##filter by this month
#     today = datetime.today()
#     currentYear = today.year
#     currentMonth = today.month
#
#     expenseItems = expenseItems.filter(expenseDate__year=currentYear,
#                                 expenseDate__month=currentMonth)
#
#     ##calculate total expense
#     totalExpense = 0
#     for expense in expenseItems:
#         totalExpense += float(expense.expenseAmt)
#
#     ##check whether there are expense stats saved
#     expenseStat = ExpenseStat.objects.all().first()
#
#     if not expenseStat:  #doesn't exist
#         totalLeft = budget - totalExpense
#         stats = ExpenseStat(totalBudget = budget,
#                             totalExpense = totalExpense,
#                             totalLeft = totalLeft)
#         stats.save()
#     else:
#         expenseStat.update(totalBudget = budget)
#         totalLeft = expenseStat.totalBudget - totalExpense
#         expenseStat.update(totalExpense = totalExpense)
#         expenseStat.update(totalLeft = totalLeft)
#
#     return render(request, "stats.html", {'expenses': expenseItems,'stats':expenseStat})
#
#     # return HttpResponseRedirect('/')
