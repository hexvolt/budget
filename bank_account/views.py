from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from bank_account.models import BankAccount
from bank_account.serializers import BankAccountSerializer


class BankAccountViewSet(viewsets.ModelViewSet):

    serializer_class = BankAccountSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    def get_queryset(self):
        return BankAccount.objects.filter(bank__user=self.request.user)

    def list(self, request, bank_pk=None, *args, **kwargs):
        queryset = self.get_queryset().filter(bank=bank_pk)
        serializer = self.serializer_class(
            queryset,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None, bank_pk=None, *args, **kwargs):
        queryset = self.get_queryset().filter(bank=bank_pk)
        bank_account = get_object_or_404(queryset, pk=pk)

        serializer = self.get_serializer(
            bank_account,
            context={'request': request}
        )
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, bank_pk=None, *args, **kwargs):
        queryset = Bank.objects.filter(user=request.user)
        bank = get_object_or_404(queryset, pk=bank_pk)
        serializer = self.get_serializer(data=request.data, bank=bank)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
