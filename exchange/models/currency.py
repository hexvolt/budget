from django.db import models


class Currency(models.Model):

    name = models.CharField(max_length=255)
    iso_code = models.CharField(max_length=3, unique=True)

    class Meta:
        db_table = 'currency'
        ordering = ['iso_code']

    def __str__(self):
        return f'{self.name}'
