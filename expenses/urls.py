from django.urls import path
from . import views  # Import the views from the same app

urlpatterns = [
    path('', views.expense_list, name='expense_list'),  # Homepage that lists expenses
    path('add/', views.expense_form, name='expense_form'),  # Form for adding an expense
    path('delete/<int:expense_id>/', views.expense_confirm_delete, name='expense_confirm_delete'),  # Confirmation to delete an expense
]
