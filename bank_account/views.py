from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from bank_account.models import BankAccount
from bank_account.serializers import BankAccountSerializer


class BankAccountViewSet(viewsets.ModelViewSet):

    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    def list(self, request, bank_pk=None):
        queryset = self.get_queryset().filter(bank=bank_pk)
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, bank_pk=None):
        queryset = self.get_queryset().filter(bank=bank_pk)
        bank_account = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer_class()(bank_account)
        return Response(serializer.data)
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    #
    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)
