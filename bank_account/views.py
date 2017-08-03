from rest_framework import viewsets
from rest_framework.filters import SearchFilter, DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from bank_account.models import BankAccount
from bank_account.serializers import BankAccountSerializer


class BankAccountViewSet(viewsets.ModelViewSet):

    serializer_class = BankAccountSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('currency',)
    search_fields = ('name',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Return only those bank accounts which belong to current user
        and which are related to the bank ID specified in the URL
        """

        bank_pk = self.kwargs['bank_pk']
        queryset = BankAccount.objects.filter(
            bank__user=self.request.user,
            bank=bank_pk
        )
        return queryset

    def get_object(self):
        """
        Returns a bank account which belongs to a certain bank
        and which ID is specified in the URL. Used by retrieve view.
        """

        bank_account = get_object_or_404(
            queryset=self.get_queryset(),
            pk=self.kwargs['pk']
        )
        return bank_account

    def perform_create(self, serializer):
        """
        Determines the bank instance from URL in order to create
        related bank account. Used by create view.
        """

        bank_pk = self.kwargs['bank_pk']
        user_banks = self.request.user.banks.all()
        bank = get_object_or_404(queryset=user_banks, pk=bank_pk)

        serializer.save(bank=bank)
