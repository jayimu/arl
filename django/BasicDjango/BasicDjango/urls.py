from django.conf.urls import url
from . import request
from . import responseCookie
from . import session
from . import user
from . import post

urlpatterns = [
    url(r'^request$', request.myRequest),
    url(r'^response$', responseCookie.myResponse),
    url(r'^writeCookie$', responseCookie.writeCookie),
    url(r'^readCookie$', responseCookie.readCookie),
    url(r'^writeSession$', session.writeSession),
    url(r'^readSession$', session.readSession),
    url(r'^$', user.index),
    url(r'^login$', user.login),
    url(r'^logout$', user.logout),
    url(r'^post$', post.myPost),

]
