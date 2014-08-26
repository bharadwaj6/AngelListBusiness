from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from search import views

urlpatterns = patterns('',
	url(r'$', 'search.views.index'),
    url(r'^index/', 'search.views.index', name='index'),
    url(r'^search/(?P<keyword>[^\.]+)/(?P<location>[^\.]+)$', 'search.views.search', name='search'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

