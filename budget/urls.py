from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    # url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('budget.urls_api')),
]
