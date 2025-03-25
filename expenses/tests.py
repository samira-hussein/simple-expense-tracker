# expenses/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Expense, Category
from decimal import Decimal

class ExpenseModelTest(TestCase):

    def setUp(self):
        # Create a user and a category for testing
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.category = Category.objects.create(name="Groceries")
        
        # Create an expense for testing
        self.expense = Expense.objects.create(
            name="Test Expense",
            amount=Decimal('10.00'),
            date="2025-03-25",
            user=self.user,
            category=self.category,
        )

    def test_expense_creation(self):
        """Test that an expense is created correctly"""
        self.assertEqual(self.expense.name, "Test Expense")
        self.assertEqual(str(self.expense.amount), '10.00')
        self.assertEqual(self.expense.user.username, 'testuser')
        self.assertEqual(self.expense.category.name, "Groceries")

    def test_category_str_method(self):
        """Test the __str__ method of Category model"""
        self.assertEqual(str(self.category), "Groceries")

class ExpenseViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_expense_list_view(self):
        """Test the expense list view"""
        # Create a category and an expense
        category = Category.objects.create(name="Travel")
        Expense.objects.create(
            name="Travel Expense",
            amount=Decimal('15.00'),
            date="2025-03-25",
            user=self.user,
            category=category
        )
        
        # Make a GET request to the expense list page
        response = self.client.get(reverse('expense_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Travel Expense")
        self.assertContains(response, "15.00")
    
    def test_expense_form_view(self):
        """Test the expense form for adding a new expense"""
        # Make a GET request to the expense form page
        response = self.client.get(reverse('expense_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'expenses/expense_form.html')
    
    def test_expense_delete_view(self):
        """Test the delete view of an expense"""
        # Create an expense to be deleted
        expense = Expense.objects.create(
            name="Expense to delete",
            amount=Decimal('25.00'),
            date="2025-03-25",
            user=self.user,
            category=self.category
        )
        
        # Make a GET request to delete the expense
        response = self.client.post(reverse('expense_confirm_delete', args=[expense.id]))
        self.assertRedirects(response, reverse('expense_list'))
        self.assertFalse(Expense.objects.filter(id=expense.id).exists())

class ExpenseFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.category = Category.objects.create(name="Food")

    def test_expense_form_valid_data(self):
        """Test the expense form with valid data"""
        data = {
            'name': 'Test Expense',
            'amount': Decimal('100.00'),
            'date': '2025-03-25',
            'category': self.category.id
        }
        form = ExpenseForm(data)
        self.assertTrue(form.is_valid())

    def test_expense_form_invalid_data(self):
        """Test the expense form with invalid data"""
        data = {
            'name': '',  # Empty name, which should be invalid
            'amount': Decimal('100.00'),
            'date': '2025-03-25',
            'category': self.category.id
        }
        form = ExpenseForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
