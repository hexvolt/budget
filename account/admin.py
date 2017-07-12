from django.contrib import admin

from account.models import Account


class AccountAdmin(admin.ModelAdmin):
    fields = ('name', 'bank', ('balance', 'currency'), 'description')
    list_display = ('name', 'bank', 'balance', 'currency')
    list_filter = ('bank', 'currency')


admin.site.register(Account, AccountAdmin)
