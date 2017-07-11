from django.db import models


class Source(models.Model):

    name = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'income_source'
        ordering = ['order', 'name']


class Income(models.Model):

    source = models.ForeignKey('income.Source',
                               related_name='incomes',
                               on_delete=models.PROTECT)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.ForeignKey('exchange.Currency',
                                 related_name='incomes',
                                 on_delete=models.PROTECT)

    date = models.DateTimeField()
    description = models.TextField()

    # to_account = models.ForeignKey('account.Account', null=True)
    # hash_tags = models.ManyToManyField()

    class Meta:
        db_table = 'income'
        ordering = ['date']
