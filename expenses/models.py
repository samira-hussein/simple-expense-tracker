from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  # Import to raise validation errors

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount with two decimal places
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # Link to Category model
    description = models.TextField(blank=True, null=True)  # Optional description for the expense

    def clean(self):
        # Custom validation to ensure the amount is not less than 0.01
        if self.amount < 0.01:
            raise ValidationError('Amount must be at least 0.01.')

    def __str__(self):
        return self.name


   