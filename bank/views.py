from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from bank.models import Bank
from bank.serializers import BankSerializer


class BankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to manage their banks.
    """

    queryset = Bank.objects.all()
    serializer_class = BankSerializer
