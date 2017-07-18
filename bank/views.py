from rest_framework import viewsets

from bank.serializers import BankSerializer


class BankViewSet(viewsets.ModelViewSet):

    serializer_class = BankSerializer

    def get_queryset(self):
        return self.request.user.banks.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
