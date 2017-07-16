from django.contrib import admin

from expense.models import ExpenseCategory, Expense


class ExpenseCategoryAdmin(admin.ModelAdmin):
    fields = ('user', ('name', 'order'),)
    list_display = ('user', 'name', 'order')
    list_filter = ('user',)


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
