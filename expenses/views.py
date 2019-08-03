from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ExpenseItem, ExpenseStat
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

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


class expenseData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        categories = ["Utilities", "Health Care", "Grocery/Restaurant", "Personal Care",
        "Entertainment", "Membership Fees", "Transportation", "Education", "Other"]

        colors = ['#F5CB5C', '#D7FDF0', '#F64740', '#A2E3C4', '#F3E9D2',
          '#52B2CF', '#F96900', '#57BC90', '#015249'];

        ##sum all of the expenses
        ##filter by this month
        today = datetime.today()
        currentYear = today.year
        currentMonth = today.month
        expenseItems = ExpenseItem.objects.all()
        expenseItems = expenseItems.filter(expenseDate__year=currentYear,expenseDate__month=currentMonth)

        ##calculate total expense
        categoryExpenses = [0]*9

        for expense in expenseItems:
            for i in range(0, 9):
                if expense.expenseCategory == categories[i]:
                    categoryExpenses[i] += float(expense.expenseAmt)
                    break

        updatedCategory = []
        updatedColor = []
        updatedExpense = []

        for i in range(0, len(categoryExpenses)):
            if categoryExpenses[i] > 0:
                updatedCategory.append(categories[i])
                updatedColor.append(colors[i])
                updatedExpense.append(categoryExpenses[i])

        data = {
            "labels": updatedCategory,
            "expenses": updatedExpense,
            "expenseColors":updatedColor
        }
        return Response(data)
