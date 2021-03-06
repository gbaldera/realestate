from django.conf.urls import *
from django.conf import settings

from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from realestate.api import PropiedadViewSet
from realestate.listing import sitemap

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'propiedades', PropiedadViewSet)

urlpatterns = patterns(
    '',
    url(r'^$', 'realestate.home.views.index', name='index'),
    url(r'^properties/$', 'realestate.listing.views.properties', name='all_properties'),
    url(r'^sale/$', 'realestate.listing.views.sale', name='properties_for_sale'),
    url(r'^sale/(?P<type>\w+)/$', 'realestate.listing.views.sale', name='properties_for_sale'),
    url(r'^rent/$', 'realestate.listing.views.rent', name='properties_for_rent'),
    url(r'^rent/(?P<type>\w+)/$', 'realestate.listing.views.rent', name='properties_for_rent'),
    url(r'^search/', 'realestate.listing.views.search', name='search'),
    url(r'^listing/(?P<slug>[\w-]+)/', 'realestate.listing.views.details', name='property_details'),
    url(r'^agents/$', 'realestate.listing.views.agents', name='agents'),
    url(r'^agents/listing/(?P<agent>[\d]+)/$', 'realestate.listing.views.agent_listings', name='agent-listings'),
    url(r'^get_map/$', 'realestate.listing.views.get_map', name='mapa-propiedades'),  # Ajax

    # Static Pages
    url(r'^about-us/$', TemplateView.as_view(template_name='home/about-us.html'), name='home_aboutus'),
    url(r'^contact/$', TemplateView.as_view(template_name='home/contact-us.html'), name='home_contact'),
    url(r'^services/$', TemplateView.as_view(template_name='home/services.html'), name='home_services'),

    # API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^api/', include(router.urls)),

    # Sitemaps
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'blog': sitemap.ListingSitemap}}),

    # Django apps
    (r'^admin/', include('realestate.admin.urls')),  # Custom Admin Site

    (r'^admin2/', include(admin.site.urls)),  # Enabling Admin
    (r'^i18n/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
