from rest_framework.serializers import HyperlinkedModelSerializer

from exchange.models import Currency


class CurrencySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Currency
        fields = (
            'id',
            'url',
            'name',
            'iso_code'
        )
