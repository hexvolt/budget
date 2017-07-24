from django.db.models import Max, Q
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.filters import SearchFilter

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

        :param queryset:
        :param name:
        :param value:
        :return:
        """

        bank_latest_dates = queryset.values('bank').\
            annotate(latest_date=Max('date')).order_by().values('id')

        q_statement = Q()

        for bank_latest_date in bank_latest_dates:
            q_statement |= (Q(bank__exact=bank_latest_date['bank'],
                              date=bank_latest_date['latest_date']))

        queryset = queryset.filter(q_statement)
        # SELECT "exchange_rate"."id", MAX("exchange_rate"."date") AS "latest_date"
        # FROM "exchange_rate" INNER JOIN "bank" ON ("exchange_rate"."bank_id" = "bank"."id")
        # WHERE "bank"."user_id" = 1 GROUP BY "exchange_rate"."bank_id"

        # with Postgres database this can be used instead:
        # queryset = queryset.order_by('bank', '-date').distinct('bank')

        return queryset


class ExchangeRateViewSet(viewsets.ModelViewSet):

    serializer_class = ExchangeRateSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ExchangeRateFilter
    # filter_fields = {
    #     'bank': ['exact'],
    #     'date': ['gte', 'lt'],
    #     'currency_from': ['exact'],
    #     'currency_to': ['exact']
    # }

    def get_queryset(self):
        return ExchangeRate.objects.filter(bank__user=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    #
    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)
