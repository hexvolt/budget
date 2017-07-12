from django.contrib import admin

from exchange.models import Currency, Conversion, ExchangeRate


class ExchangeRateAdmin(admin.ModelAdmin):
    fields = ('bank', 'date', ('currency_from', 'rate', 'currency_to'))
    list_display = ('bank', 'date', 'direction', 'rate')
    list_filter = ('bank',)


admin.site.register(ExchangeRate, ExchangeRateAdmin)

admin.site.register((Currency, Conversion))
