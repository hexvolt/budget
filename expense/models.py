from django.db import models


class Category(models.Model):

    name = models.CharField()


class Expense(models.Model):

    category = models.ForeignKey('expense.Category')

    amount = models.DecimalField()
    currency = models.ForeignKey('exchange.Currency')

    date = models.DateTimeField()
    description = models.CharField()

    # from_account = models.ForeignKey('account.Account')
    # hash_tags
