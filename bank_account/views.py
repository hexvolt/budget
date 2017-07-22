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

        bank_accounts = self.get_queryset().filter(bank=bank_pk)
        serializer = self.get_serializer(
            bank_accounts,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, bank_pk=None, pk=None, *args, **kwargs):

        # getting a certain bank_account using IDs from URL
        bank_accounts = self.get_queryset().filter(bank=bank_pk)
        bank_account = get_object_or_404(queryset=bank_accounts, pk=pk)

        serializer = self.get_serializer(
            bank_account,
            context={'request': request}
        )
        return Response(serializer.data)

    def perform_create(self, serializer):

        # getting the bank using its ID taken from URL
        bank_pk = self.kwargs['bank_pk']
        user_banks = self.request.user.banks.all()
        bank = get_object_or_404(queryset=user_banks, pk=bank_pk)

        serializer.save(bank=bank)
