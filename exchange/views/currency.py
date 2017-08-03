from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from exchange.models import Currency
from exchange.serializers import CurrencySerializer


class CurrencyViewSet(viewsets.ModelViewSet):

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'iso_code')
    http_method_names = ('get', 'head')
