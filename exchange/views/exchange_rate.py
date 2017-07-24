from django.db import connection
from django.db.models import Max, F
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from rest_framework import viewsets

from exchange.models import ExchangeRate
from exchange.serializers import ExchangeRateSerializer


class ExchangeRateFilter(filters.FilterSet):

    latest_per_bank = filters.BooleanFilter(method='filter_latest_per_bank')

    class Meta:
        model = ExchangeRate
        fields = {
            'bank': ['exact'],
            'date': ['gte', 'lt'],
            'currency_from': ['exact'],
            'currency_to': ['exact'],
            'latest_per_bank': ['exact']
        }

    def filter_latest_per_bank(self, queryset, name, value):
        """
        Returns the latest ExchangeRates for each bank
        present in the queryset.
        """

        if connection.vendor == 'postgresql':
            # Postgres supports DISTINCT ON construction, so this is the
            # most efficient way to obtain the latest rates per bank

            queryset = queryset.order_by('bank', '-date').distinct('bank')

        else:
            # As other databases do not support DISTINCT operation on a
            # certain field, we compute the latest date manually. This
            # query is fairly inefficient in terms of performance, but
            # this is the most elegant Django ORM construction which allows
            # to avoid for-loops or raw SQL queries.

            queryset = queryset.annotate(
                latest_date=Max('bank__exchange_rates__date')
            ).filter(date=F('latest_date'))

        return queryset


class ExchangeRateViewSet(viewsets.ModelViewSet):

    serializer_class = ExchangeRateSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ExchangeRateFilter

    def get_queryset(self):
        return ExchangeRate.objects.filter(bank__user=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    #
    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)
