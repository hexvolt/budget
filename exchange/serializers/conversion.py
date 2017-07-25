from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ValidationError
)

from exchange.models import Conversion, Currency


class ConversionSerializer(HyperlinkedModelSerializer):

    currency_from = SlugRelatedField(queryset=Currency.objects.all(),
                                     slug_field='iso_code')

    currency_to = SlugRelatedField(queryset=Currency.objects.all(),
                                   slug_field='iso_code')

    class Meta:
        model = Conversion
        fields = (
            'id',
            'url',
            'date',
            'amount_from',
            'currency_from',
            'amount_to',
            'currency_to',
            'description',
        )

    def validate(self, attrs):
        """
        Make sure that currency_from and currency_to are different values
        """

        if attrs['currency_from'] == attrs['currency_to']:
            raise ValidationError('Currencies must be different')

        return attrs
