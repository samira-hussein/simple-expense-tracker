# expenses/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail  # For email notifications, optional
from .models import Expense

# Signal to notify the user when an Expense is created or updated
@receiver(post_save, sender=Expense)
def notify_expense_created_or_updated(sender, instance, created, **kwargs):
    if created:
        action = "created"
    else:
        action = "updated"
    
    # Send an email or notification (optional: you can also push it to the frontend)
    send_mail(
        'Expense Notification',
        f'Your expense titled "{instance.name}" has been {action}.',
        'noreply@example.com',  # From email
        [instance.user.email],  # To the user's email
        fail_silently=False,
    )
    print(f"Notification: Expense {action} for user {instance.user.username}")

# Signal to notify the user when an Expense is deleted
@receiver(post_delete, sender=Expense)
def notify_expense_deleted(sender, instance, **kwargs):
    send_mail(
        'Expense Deletion Notification',
        f'Your expense titled "{instance.name}" has been deleted.',
        'noreply@example.com',
        [instance.user.email],
        fail_silently=False,
    )
    print(f"Notification: Expense deleted for user {instance.user.username}")
