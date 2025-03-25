from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),  # URL for viewing the list of expenses
    path('add/', views.expense_form, name='expense_form'),  # URL for adding an expense
    path('edit/<int:expense_id>/', views.expense_form, name='expense_edit'),  # URL for editing an expense
    path('delete/<int:expense_id>/', views.expense_confirm_delete, name='expense_confirm_delete'),  # URL for confirming deletion of an expense
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login URL (using Django's built-in login view)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL (using Django's built-in logout view)
    path('register/', views.register, name='register'),  # Registration URL (user-created view)
]
