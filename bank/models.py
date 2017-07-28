from django.conf import settings
from django.db import models


class Bank(models.Model):
    """
    Represents a bank where user have certain accounts.

    Each user have at least one Bank instance named 'Cash'
    for storing cash accounts.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='banks',
                             on_delete=models.CASCADE)

    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'bank'
        unique_together = ('user', 'name')
        ordering = ['user', 'name']

    def __str__(self):
        return f'{self.name} ({self.user})'
