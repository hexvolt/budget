from django.conf.urls import url, include
from rest_framework import routers

import bank.views


router = routers.DefaultRouter()
router.register(r'banks', bank.views.BankViewSet, base_name='bank')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
]
