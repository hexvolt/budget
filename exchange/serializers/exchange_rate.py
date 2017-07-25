from rest_framework.relations import (
    PrimaryKeyRelatedField,
    SlugRelatedField
)
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ValidationError
)

from bank.models import Bank
from exchange.models import ExchangeRate, Currency


class ExchangeRateSerializer(HyperlinkedModelSerializer):

    bank = PrimaryKeyRelatedField(queryset=Bank.objects.none())

    currency_from = SlugRelatedField(queryset=Currency.objects.all(),
                                     slug_field='iso_code')

    currency_to = SlugRelatedField(queryset=Currency.objects.all(),
                                   slug_field='iso_code')

    class Meta:
        model = ExchangeRate
        fields = (
            'id',
            'url',
            'bank',
            'date',
            'rate',
            'currency_from',
            'currency_to',
        )

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request')

        self.fields['bank'].queryset = Bank.objects.filter(user=request.user)

        super(ExchangeRateSerializer, self).__init__(*args, **kwargs)

    def validate(self, attrs):
        """
        Make sure that currency_from and currency_to are different values
        """

        if attrs['currency_from'] == attrs['currency_to']:
            raise ValidationError('Currencies must be different')

        return attrs
