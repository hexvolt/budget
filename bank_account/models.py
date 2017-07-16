from django.db import models


class BankAccount(models.Model):

    bank = models.ForeignKey('bank.Bank',
                             related_name='accounts',
                             on_delete=models.PROTECT)

    balance = models.DecimalField(max_digits=12, decimal_places=2)

    currency = models.ForeignKey('exchange.Currency',
                                 related_name='bank_accounts',
                                 on_delete=models.PROTECT)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # account_type (deposit, card, saving, etc)

    class Meta:
        db_table = 'bank_account'
        unique_together = ('bank', 'name')

    def __str__(self):
        return f'{self.name} at {self.bank} ({self.currency})'
