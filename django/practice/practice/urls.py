
from django.conf.urls import url
from . import solution1
from . import solution2
urlpatterns = [
    url(r'^solution1$', solution1.solution1),
    url(r'^solution2$', solution2.solution2),
]
