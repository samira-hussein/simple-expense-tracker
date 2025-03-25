from django import forms
from .models import Expense

CATEGORY_CHOICES = [
    ('travel', 'Travel'),
    ('groceries', 'Groceries'),
    ('rent', 'Rent'),
    ('car', 'Car'),
    ('mortgage', 'Mortgage'),
    ('repair', 'Repair'),
    ('other', 'Other'),
    ('take_out', 'Take Out'),
]

class ExpenseForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True)

    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date', 'category']

    def save(self, commit=True):
        expense = super().save(commit=False)
        if commit:
            expense.save()
        return expense
