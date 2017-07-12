from django.contrib import admin

from expense.models import Category, Expense


class CategoryAdmin(admin.ModelAdmin):
    fields = (('name', 'order'),)
    list_display = ('name', 'order')


class ExpenseAdmin(admin.ModelAdmin):
    fields = ('category', ('amount', 'currency'), 'date', 'description')
    list_display = ('category', 'date', 'amount', 'currency', 'description')
    list_filter = ('category', 'currency')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Expense, ExpenseAdmin)
