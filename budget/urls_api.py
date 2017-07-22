from django.conf.urls import url, include
from rest_framework_nested import routers

import bank.views
import bank_account.views


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
    base_name='bankaccount'  # set view/URL names as 'bankaccount-list', etc
)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(banks_account_router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
]
