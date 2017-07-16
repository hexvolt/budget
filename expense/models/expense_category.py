from django.conf import settings
from django.db import models


class ExpenseCategory(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='expense_categories',
                             on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'expense_category'
        unique_together = ('user', 'name')
        ordering = ['user', 'order', 'name']

    def __str__(self):
        return f'{self.name} ({self.user})'