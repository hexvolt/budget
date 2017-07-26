from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from expense.models import Expense
from expense.serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):

    serializer_class = ExpenseSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description',)

    def get_queryset(self):
        return Expense.objects.filter(expense_category__user=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    #
    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)
