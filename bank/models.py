from django.db import models


class Bank(models.Model):

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'bank'

    def __str__(self):
        return f'{self.name}'
