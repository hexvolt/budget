from django.conf import settings
from django.db import models


class IncomeSource(models.Model):
    """
    An income source (e.g. "Salary", "Gifts", etc).

    Each user defines his own income sources.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='income_sources',
                             on_delete=models.CASCADE)

    name = models.CharField(max_length=255,
                            help_text='An income source (e.g. "Salary", '
                                      '"Gifts", etc).')
    order = models.PositiveSmallIntegerField(
        default=0, help_text='An order this income source will be displayed '
                             'among the other ones'
    )

    class Meta:
        db_table = 'income_source'
        unique_together = ('user', 'name')
        ordering = ['user', 'order', 'name']

    def __str__(self):
        return f'{self.name} ({self.user})'
