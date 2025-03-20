from django.shortcuts import render
from django.http import HttpResponse
from .models import Expense  # Import the Expense model

# Home page (optional)
def index(request):
    return HttpResponse("Welcome to the Simple Expense Tracker!")

# View for listing all expenses
def expense_list(request):
    expenses = Expense.objects.all()  # Fetch all expenses from the database
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})  # Pass expenses to the template

# View for adding or updating an expense (form view)
def expense_form(request):
    # Handle form submission logic here (you can add form handling in the future)
    return render(request, 'expenses/expense_form.html')

# View for confirming deletion of an expense
def expense_confirm_delete(request, expense_id):
    expense = Expense.objects.get(id=expense_id)  # Fetch the expense by its ID
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})  # Pass the expense to the template
