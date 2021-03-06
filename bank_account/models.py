from django.db import models


class BankAccount(models.Model):
    """
    Represents a current state of a certain user's account.

    It is supposed to be periodically updated by user in order
    to calculate deficits.
    """

    bank = models.ForeignKey('bank.Bank',
                             related_name='accounts',
                             on_delete=models.PROTECT)

    balance = models.DecimalField(max_digits=12,
                                  decimal_places=2,
                                  help_text='Current balance')

    currency = models.ForeignKey('exchange.Currency',
                                 related_name='bank_accounts',
                                 on_delete=models.PROTECT)

    name = models.CharField(max_length=255,
                            help_text='A distinguishable name of your account '
                                      '(e.g. "Visa 0XXX", "Deposit")')
    description = models.TextField(blank=True)

    # account_type (deposit, card, saving, etc)

    class Meta:
        db_table = 'bank_account'
        unique_together = ('bank', 'name')

    def __str__(self):
        return f'{self.name} at {self.bank} ({self.currency})'
