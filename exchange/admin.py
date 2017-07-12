from django.contrib import admin
from exchange.models import Currency, Conversion, ExchangeRate


class ConversionAdmin(admin.ModelAdmin):
    fields = (
        ('amount_from', 'currency_from'),
        ('amount_to', 'currency_to'),
        'date'
    )
    list_display = ('date', 'sold', 'bought')

    def sold(self, obj):
        return f'{obj.amount_from} {obj.currency_from}'

    def bought(self, obj):
        return f'{obj.amount_to} {obj.currency_to}'


class ExchangeRateAdmin(admin.ModelAdmin):
    fields = ('bank', 'date', ('currency_from', 'rate', 'currency_to'))
    list_display = ('bank', 'date', 'direction', 'rate')
    list_filter = ('bank',)


admin.site.register(Conversion, ConversionAdmin)
admin.site.register(Currency)
admin.site.register(ExchangeRate, ExchangeRateAdmin)

