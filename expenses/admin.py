from django.contrib import admin
from .models import Expense  # Import the Expense model

admin.site.register(Expense)  # Register the Expense model with the admin site
