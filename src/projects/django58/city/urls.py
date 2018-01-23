"""city URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import view

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^$', view.index),
    url(r'^index/$', view.index),
    url(r'^login/$', view.login),
    url(r'^logout/$', view.logout),
    url(r'^register/$', view.register),
    url(r'^recruitment/$', view.recruitment),
    url(r'^recList/$', view.recList),
    url(r'^apply/$', view.apply),
    url(r'^recDetails/$', view.recDetails),
    url(r'^carList/$', view.carList),
    url(r'^carAjaxInfo/$', view.carAjaxInfo),
]