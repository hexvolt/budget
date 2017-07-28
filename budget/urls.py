from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    # url(r'^$', landing_page),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('budget.urls_api')),
    url(r'^api-auth/', include('rest_framework.urls'))
]
