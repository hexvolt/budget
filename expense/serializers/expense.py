from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from expense.models import Expense, ExpenseCategory
from exchange.models import Currency


class ExpenseSerializer(HyperlinkedModelSerializer):

    expense_category = SlugRelatedField(
        queryset=ExpenseCategory.objects.none(),
        slug_field='name'
    )

    currency = SlugRelatedField(
        queryset=Currency.objects.all(),
        slug_field='iso_code'
    )

    class Meta:
        model = Expense
        fields = (
            'id',
            'url',
            'expense_category',
            'date',
            'amount',
            'currency',
            'description',
        )

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request')

        user_categories = ExpenseCategory.objects.filter(user=request.user)
        self.fields['expense_category'].queryset = user_categories

        super(ExpenseSerializer, self).__init__(*args, **kwargs)
