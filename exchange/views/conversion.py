from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from rest_framework import viewsets

from exchange.serializers import ConversionSerializer


class ConversionViewSet(viewsets.ModelViewSet):

    serializer_class = ConversionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = (
        'currency_from',
        'currency_to',
    )

    def get_queryset(self):
        return self.request.user.conversions.all()
