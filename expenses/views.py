from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm  # Import the ExpenseForm to handle form logic
from django.contrib.auth.decorators import login_required  # Import login_required to protect views
from django.contrib.auth import get_user_model  # To access the user model if needed

# View for listing all expenses
@login_required  # Only logged-in users can access this view
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)  # Fetch expenses only for the logged-in user
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})  # Pass expenses to the template

# View for adding or updating an expense (form view)
@login_required  # Only logged-in users can access this view
def expense_form(request, expense_id=None):
    if expense_id:  # If there's an ID, it's an edit operation
        expense = get_object_or_404(Expense, pk=expense_id, user=request.user)  # Ensure the expense belongs to the logged-in user
    else:  # Otherwise, it's a create operation
        expense = None

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)  # If editing, instance will be the expense
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Associate the expense with the logged-in user
            expense.save()  # Save the form data to the database
            return redirect('expense_list')  # Redirect to the list of expenses after saving
    else:
        form = ExpenseForm(instance=expense)  # Pre-fill the form if editing

    return render(request, 'expenses/expense_form.html', {'form': form})

# View for confirming deletion of an expense
@login_required  # Only logged-in users can access this view
def expense_confirm_delete(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id, user=request.user)  # Fetch the expense to delete, ensuring it's the user's expense

    if request.method == 'POST':  # If the form is submitted, delete the expense
        expense.delete()
        return redirect('expense_list')  # Redirect to the list of expenses after deletion

    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})

# User registration view (if needed)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('expense_list')  # Redirect to the expense list after registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

