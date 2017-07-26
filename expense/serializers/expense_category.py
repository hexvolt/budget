from rest_framework.serializers import HyperlinkedModelSerializer

from expense.models import ExpenseCategory


class ExpenseCategorySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = ExpenseCategory
        fields = (
            'id',
            'url',
            'name',
            'order'
        )
