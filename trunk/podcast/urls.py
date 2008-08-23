from django.conf.urls.defaults import *

urlpatterns = patterns('podcast.views',
    # Show list of all shows
    (r'^$', 'show_list'),

    # Episode list of one show
    (r'^(?P<slug>[-\w]+)/$', 'episode_list'),

    # Episode list feed by show
    (r'^(?P<slug>[-\w]+)/feed/$', 'show_list_feed'),

    # Episode detail of one show
    (r'^(?P<show_slug>[-\w]+)/(?P<episode_slug>[-\w]+)/$', 'episode_detail'),

    # Episode sitemap list of one show
    (r'^(?P<slug>[-\w]+)/sitemap.xml$', 'episode_sitemap'),
)