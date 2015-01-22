from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

import djangousers.views

urlpatterns = patterns('',
    url(r'^$', djangousers.views.ListContactView.as_view(),
        name='contacts-list',),
    url(r'^new$', djangousers.views.CreateContactView.as_view(),
        name='contacts-new',),
    url(r'^edit/(?P<pk>\d+)/$', djangousers.views.UpdateContactView.as_view(),
        name='contacts-edit',),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
