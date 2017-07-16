from django.contrib import admin

from bank_account.models import BankAccount


class BankAccountAdmin(admin.ModelAdmin):
    fields = ('name', 'bank', ('balance', 'currency'), 'description')
    list_display = ('name', 'bank', 'owner', 'balance', 'currency')
    list_filter = ('bank', 'currency')

    @staticmethod
    def owner(obj):
        return obj.bank.user


admin.site.register(BankAccount, BankAccountAdmin)
