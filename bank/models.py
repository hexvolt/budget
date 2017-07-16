from django.conf import settings
from django.db import models


class Bank(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='bank_accounts',
                             on_delete=models.CASCADE)

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'bank'
        unique_together = ('user', 'name')

    def __str__(self):
        return f'{self.name}'
