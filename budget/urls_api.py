from django.conf.urls import url, include
from rest_framework_nested import routers

import bank.views
import bank_account.views


router = routers.DefaultRouter()
router.register(
    prefix=r'banks',
    viewset=bank.views.BankViewSet,
    base_name='bank'
)

banks_account_router = routers.NestedSimpleRouter(
    parent_router=router,
    parent_prefix=r'banks',
    lookup='bank'
)
banks_account_router.register(
    prefix=r'accounts',
    viewset=bank_account.views.BankAccountViewSet,
    base_name='account'
)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(banks_account_router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
]
