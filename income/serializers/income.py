from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from income.models import Income, IncomeSource
from exchange.models import Currency


class IncomeSerializer(HyperlinkedModelSerializer):

    income_source = SlugRelatedField(
        queryset=IncomeSource.objects.none(),
        slug_field='name'
    )

    currency = SlugRelatedField(
        queryset=Currency.objects.all(),
        slug_field='iso_code'
    )

    class Meta:
        model = Income
        fields = (
            'id',
            'url',
            'income_source',
            'date',
            'amount',
            'currency',
            'description',
        )

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request')

        user_sources = IncomeSource.objects.filter(user=request.user)
        self.fields['income_source'].queryset = user_sources

        super(IncomeSerializer, self).__init__(*args, **kwargs)
