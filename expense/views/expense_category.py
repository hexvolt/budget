from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from expense.serializers import ExpenseCategorySerializer


class ExpenseCategoryViewSet(viewsets.ModelViewSet):

    serializer_class = ExpenseCategorySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    def get_queryset(self):
        return self.request.user.expense_categories.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
