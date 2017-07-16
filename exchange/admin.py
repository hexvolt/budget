from django.contrib import admin
from exchange.models import Currency, Conversion, ExchangeRate


class ConversionAdmin(admin.ModelAdmin):
    fields = (
        'user',
        ('amount_from', 'currency_from'),
        ('amount_to', 'currency_to'),
        'date'
    )
    list_display = ('user', 'date', 'sold', 'bought')
    list_filter = ('user',)

    @staticmethod
    def sold(obj):
        return f'{obj.amount_from} {obj.currency_from}'

    @staticmethod
    def bought(obj):
        return f'{obj.amount_to} {obj.currency_to}'


class CurrencyAdmin(admin.ModelAdmin):
    fields = (('name', 'iso_code'),)
    list_display = ('name', 'iso_code')


class ExchangeRateAdmin(admin.ModelAdmin):
    fields = ('bank', 'date', ('currency_from', 'rate', 'currency_to'))
    list_display = ('bank', 'date', 'direction', 'rate')
    list_filter = ('bank',)


admin.site.register(Conversion, ConversionAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ExchangeRate, ExchangeRateAdmin)

