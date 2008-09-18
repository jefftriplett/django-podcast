from django.conf.urls.defaults import *

urlpatterns = patterns('podcast.views',
    # Show list of all shows
    (r'^$', 'show_list'),

    # Episode list of one show
    (r'^(?P<slug>[-\w]+)/$', 'episode_list'),

    # Episode list feed by show (RSS 2.0 and iTunes)
    url(r'^(?P<slug>[-\w]+)/feed/$', 'show_list_feed', name='show_list_feed'),

    # Episode list feed by show (Atom)
    (r'^(?P<slug>[-\w]+)/atom/$', 'show_list_feed'),
    
    # Episode list feed by show (Media RSS)
    (r'^(?P<slug>[-\w]+)/media/$', 'show_list_feed'),

    # Episode list feed by show (Photocast)
    (r'^(?P<slug>[-\w]+)/photocast/$', 'show_list_feed'),

    # Episode detail of one show
    (r'^(?P<show_slug>[-\w]+)/(?P<episode_slug>[-\w]+)/$', 'episode_detail'),

    # Episode sitemap list of one show
    (r'^(?P<slug>[-\w]+)/sitemap.xml$', 'episode_sitemap'),
)