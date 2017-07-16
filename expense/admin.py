from django.contrib import admin

from expense.models import ExpenseCategory, Expense


class ExpenseCategoryAdmin(admin.ModelAdmin):
    fields = (('name', 'order'),)
    list_display = ('name', 'order')


class ExpenseAdmin(admin.ModelAdmin):
    fields = (
        'expense_category',
        ('amount', 'currency'),
        'date',
        'description'
    )
    list_display = (
        'expense_category',
        'date',
        'amount',
        'currency',
        'description'
    )
    list_filter = ('expense_category', 'currency')


admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(Expense, ExpenseAdmin)
