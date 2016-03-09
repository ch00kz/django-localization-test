from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = i18n_patterns('',
     url(r'^$', 'translation.views.home', name='home'),
    # url(r'^admin/', include(admin.site.urls)),
)
