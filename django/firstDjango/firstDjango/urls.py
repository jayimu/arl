from django.conf.urls import url
from . import First

urlpatterns = [
    url(r'^$', First.hello),

    url(r'^your$', First.your),
    url(r'^product\d+$', First.product),
    url(r'^country/China|America$', First.country),
]
