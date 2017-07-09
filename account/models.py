from django.db import models


class Account(models.Model):

    bank = models.ForeignKey('bank.Bank', related_name='accounts')

    amount = models.DecimalField()
    currency = models.ForeignKey('exchange.Currency')

    name = models.CharField()
    description = models.CharField()
    # account type (deposit, card, saving, etc)


class Transfer(models.Model):

    account_from = models.ForeignKey('account.Account')
    account_to = models.ForeignKey('account.Account')
    amount = models.DecimalField()

    # def type_(self):
    #     return 'withdrawal'
