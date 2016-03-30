from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'resultanalysis.views.group_prom', name='groupstats'),
    url(r'^(?P<group>[-\w]+)/$','resultanalysis.views.group_prom', name='groupstats'),
) 
