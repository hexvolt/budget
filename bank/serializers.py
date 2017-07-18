from bank.models import Bank
from rest_framework import serializers


class BankSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bank
        fields = ('url', 'name', )