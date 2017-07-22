from rest_framework.relations import SlugRelatedField
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from bank_account.models import BankAccount
from exchange.models import Currency


class BankAccountSerializer(NestedHyperlinkedModelSerializer):

    currency = SlugRelatedField(queryset=Currency.objects.all(),
                                slug_field='iso_code')

    class Meta:
        model = BankAccount
        fields = (
            'id',
            'url',
            'name',
            'description',
            'balance',
            'currency'
        )

    parent_lookup_kwargs = {
        'bank_pk': 'bank__pk',
    }
