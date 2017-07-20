from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.relations import StringRelatedField

from bank_account.models import BankAccount


class BankAccountSerializer(HyperlinkedModelSerializer):

    currency = StringRelatedField()

    class Meta:
        model = BankAccount
        fields = ('id', 'url', 'name', 'description', 'balance', 'currency')
