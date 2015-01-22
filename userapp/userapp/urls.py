from django.conf.urls import patterns, include, url
from django.contrib import admin

import djangousers.views

urlpatterns = patterns('',
    url(r'^$', djangousers.views.ListContactView.as_view(),
        name='contacts-list',),
    url(r'^new$', djangousers.views.CreateContactView.as_view(),
        name='contacts-new',),
    url(r'^admin/', include(admin.site.urls)),
)
