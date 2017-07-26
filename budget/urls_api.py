from django.conf.urls import url, include
from rest_framework_nested import routers

import bank.views
import bank_account.views
import exchange.views
import expense.views
import income.views


# '^/banks/$'
# '^/banks/{pk}/$'
router = routers.DefaultRouter()
router.register(
    prefix=r'banks',          # URLs for this resource will be '.../banks/...'
    viewset=bank.views.BankViewSet,
    base_name='bank'          # set view/URL names as 'bank-list', etc
)

# '^/banks/{bank_pk}/accounts/$'
# '^/banks/{bank_pk}/accounts/{pk}/$'
banks_account_router = routers.NestedSimpleRouter(
    parent_router=router,     # a parent router to attach to
    parent_prefix=r'banks',   # an end-point of parent router to attach to
    lookup='bank'             # let a variable for parent resource be 'bank_pk'
)
banks_account_router.register(
    prefix=r'accounts',       # a nested part of URL will be '.../accounts/...'
    viewset=bank_account.views.BankAccountViewSet,
    base_name='bankaccount'   # set view/URL names as 'bankaccount-list', etc
)

# '^/currencies/$'
# '^/currencies/{pk}/$'
router.register(
    prefix=r'currencies',
    viewset=exchange.views.CurrencyViewSet,
    base_name='currency'      # set view/URL names as 'currency-list', etc
)

# '^/exchange_rates/$'
# '^/exchange_rates/{pk}/$'
router.register(
    prefix=r'exchange_rates',
    viewset=exchange.views.ExchangeRateViewSet,
    base_name='exchangerate'  # set view/URL names as 'exchangerate-list', etc
)

# '^/conversions/$'
# '^/conversions/{pk}/$'
router.register(
    prefix=r'conversions',
    viewset=exchange.views.ConversionViewSet,
    base_name='conversion'    # set view/URL names as 'conversion-list', etc
)

# '^/expense_categories/$'
# '^/expense_categories/{pk}/$'
router.register(
    prefix=r'expense_categories',
    viewset=expense.views.ExpenseCategoryViewSet,
    base_name='expensecategory'
)

# '^/expenses/$'
# '^/expenses/{pk}/$'
router.register(
    prefix=r'expenses',
    viewset=expense.views.ExpenseViewSet,
    base_name='expense'
)

# '^/income_sources/$'
# '^/income_sources/{pk}/$'
router.register(
    prefix=r'income_sources',
    viewset=income.views.IncomeSourceViewSet,
    base_name='incomesource'
)

# '^/incomes/$'
# '^/incomes/{pk}/$'
router.register(
    prefix=r'incomes',
    viewset=income.views.IncomeViewSet,
    base_name='income'
)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(banks_account_router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
]
