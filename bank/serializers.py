from rest_framework.serializers import HyperlinkedModelSerializer

from bank.models import Bank
from bank_account.serializers import BankAccountSerializer


class BankSerializer(HyperlinkedModelSerializer):

    accounts = BankAccountSerializer(many=True, read_only=True)

    class Meta:
        model = Bank
        fields = (
            'id',
            'url',
            'name',
            'accounts'
        )
