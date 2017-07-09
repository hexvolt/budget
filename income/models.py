from django.db import models


class Source(models.Model):

    name = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'income_source'
        ordering = ['order', 'name']


class Income(models.Model):

    source = models.ForeignKey('income.Source', related_name='incomes', on_delete=models.CASCADE)

    amount = models.DecimalField()
    currency = models.ForeignKey('exchange.Currency')

    date = models.DateTimeField()
    description = models.CharField()

    # to_account = models.ForeignKey('account.Account') ??? account instead of currenyc?
    # hash_tags

    class Meta:
        db_table = 'income'
        ordering = ['date']
