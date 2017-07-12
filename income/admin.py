from django.contrib import admin

from income.models import Source, Income


class IncomeAdmin(admin.ModelAdmin):
    fields = ('source', ('amount', 'currency'), 'date', 'description')
    list_display = ('source', 'date', 'amount', 'currency', 'description')
    list_filter = ('source', 'currency')


class SourceAdmin(admin.ModelAdmin):
    fields = (('name', 'order'),)
    list_display = ('name', 'order')


admin.site.register(Income, IncomeAdmin)
admin.site.register(Source, SourceAdmin)
