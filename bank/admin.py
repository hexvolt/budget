from django.contrib import admin

from bank.models import Bank


class BankAdmin(admin.ModelAdmin):
    fields = ('user', 'name')
    list_display = ('user', 'name')
    list_filter = ('user',)


admin.site.register(Bank, BankAdmin)

