from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Demo.views.home', name='home'),
    # url(r'^Demo/', include('Demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
#     (r'^$', direct_to_template, {'template': 'index.html'}),
     (r'^$', TemplateView.as_view(template_name = 'index.html'}),
     (r'^beers/$', 'beer.viwes.BeerAll'),
     (r'^beers/(?P<beerslug>.*)/$', 'beer.views.SpecificBeer'),
     (r'^brewerys/(?P<breweryslug>.*)/$', 'beer.views.SpecificBrewery'),
)
