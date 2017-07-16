from django.contrib import admin

from income.models import IncomeSource, Income


class IncomeAdmin(admin.ModelAdmin):
    fields = (
        'income_source',
        ('amount', 'currency'),
        'date',
        'description'
    )
    list_display = (
        'income_source',
        'date',
        'amount',
        'currency',
        'description'
    )
    list_filter = ('income_source', 'currency')


class IncomeSourceAdmin(admin.ModelAdmin):
    fields = (('name', 'order'),)
    list_display = ('name', 'order')


admin.site.register(Income, IncomeAdmin)
admin.site.register(IncomeSource, IncomeSourceAdmin)
