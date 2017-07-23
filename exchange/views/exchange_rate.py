from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from exchange.models import ExchangeRate
from exchange.serializers import ExchangeRateSerializer


class ExchangeRateViewSet(viewsets.ModelViewSet):

    serializer_class = ExchangeRateSerializer
    # filter_backends = (SearchFilter,)
    # search_fields = ('name', 'iso_code')

    def get_queryset(self):
        return ExchangeRate.objects.filter(bank__user=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    #
    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)
