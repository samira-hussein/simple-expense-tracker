# Generated by Django 4.2.19 on 2025-03-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_category_expense_user_expense_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
