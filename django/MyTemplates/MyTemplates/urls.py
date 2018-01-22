
from django.conf.urls import url
from . import view
from . import condition
from . import iteration
from . import filter

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^condition$', condition.myCondition),
    url(r'^for$', iteration.myFor),
    url(r'^filter$',filter.myFilter)
]
