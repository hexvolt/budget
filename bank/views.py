from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from bank.serializers import BankSerializer


class BankViewSet(viewsets.ModelViewSet):

    serializer_class = BankSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.banks.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
