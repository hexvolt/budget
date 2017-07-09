from django.db import models


class Account(models.Model):

    bank = models.ForeignKey('bank.Bank', related_name='accounts', on_delete=models.PROTECT)

    amount = models.DecimalField()
    currency = models.ForeignKey('exchange.Currency', related_name='accounts', on_delete=models.PROTECT)

    name = models.CharField(max_length=255)
    description = models.TextField()
    # account type (deposit, card, saving, etc)

    class Meta:
        db_table = 'account'


# class Transfer(models.Model):
#
#     account_from = models.ForeignKey('account.Account', related_name='transfers_from', on_delete=models.PROTECT)
#     account_to = models.ForeignKey('account.Account', related_name='transfers_to', on_delete=models.PROTECT)
#     amount = models.DecimalField()
#
    # def type_(self):
    #     return 'withdrawal'

    # class Meta:
    #     db_table = 'transfer'
