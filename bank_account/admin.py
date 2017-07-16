from django.contrib import admin

from bank_account.models import BankAccount


class BankAccountAdmin(admin.ModelAdmin):
    fields = ('name', 'bank', ('balance', 'currency'), 'description')
    list_display = ('name', 'bank', 'balance', 'currency')
    list_filter = ('bank', 'currency')


admin.site.register(BankAccount, BankAccountAdmin)
