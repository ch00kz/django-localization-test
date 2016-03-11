from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from views import ArticleView, AuthorCreate

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    '',
    url(r'^$', 'translation.views.home', name='home'),
    url(r'^article/(?P<pk>\d+)/$', ArticleView.as_view(), name='article'),
    url(r'^article/create/$', AuthorCreate.as_view(), name='create-article'),
    url(r'^admin/', include(admin.site.urls)),
)
