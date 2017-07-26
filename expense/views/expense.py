from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from expense.models import Expense
from expense.serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):

    serializer_class = ExpenseSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = {
        'expense_category': ['exact'],
        'date': ['gte', 'lt'],
        'currency': ['exact'],
    }
    search_fields = ('description',)

    def get_queryset(self):
        return Expense.objects.filter(expense_category__user=self.request.user)
