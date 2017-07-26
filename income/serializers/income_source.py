from rest_framework.serializers import HyperlinkedModelSerializer

from income.models import IncomeSource


class IncomeSourceSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = IncomeSource
        fields = (
            'id',
            'url',
            'name',
            'order'
        )
