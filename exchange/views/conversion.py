from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from exchange.serializers import ConversionSerializer


class ConversionViewSet(viewsets.ModelViewSet):

    serializer_class = ConversionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = {
        'date': ['gte', 'lt'],
        'currency_from': ['exact'],
        'currency_to': ['exact']
    }
    search_fields = ('description',)

    def get_queryset(self):
        return self.request.user.conversions.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
