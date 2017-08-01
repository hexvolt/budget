from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from income.models import Income
from income.serializers import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):

    serializer_class = IncomeSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = {
        'income_source': ['exact'],
        'date': ['gte', 'lt'],
        'currency': ['exact'],
    }
    search_fields = ('description',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Income.objects.filter(income_source__user=self.request.user)
