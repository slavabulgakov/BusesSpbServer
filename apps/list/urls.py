from django.conf.urls.defaults import patterns, include, url
#from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'busesspb.views.home', name='home'),
    # url(r'^busesspb/', include('busesspb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^echo/', views.echo),
    (r'^version/', views.version),
    (r'^auth/', views.auth),
    (r'^', views.root),
)
