from django.conf.urls import patterns, include, url
from django.contrib import admin

import djangousers.views

urlpatterns = patterns('',
    url(r'^$', djangousers.views.ListContactView.as_view(),
        name='contact_list',),
    url(r'^admin/', include(admin.site.urls)),
)
