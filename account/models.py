from django.db import models


class Account(models.Model):

    bank = models.ForeignKey('bank.Bank', related_name='accounts', on_delete=models.PROTECT)

    balance = models.DecimalField()
    currency = models.ForeignKey('exchange.Currency', related_name='accounts', on_delete=models.PROTECT)

    name = models.CharField(max_length=255)
    description = models.TextField()

    # account_type (deposit, card, saving, etc)

    class Meta:
        db_table = 'account'
