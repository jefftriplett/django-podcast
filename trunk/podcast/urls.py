from django.conf.urls.defaults import *


urlpatterns = patterns('podcast.views',
    # Show list of all shows
    url(r'^$', view='show_list', name='podcast_shows'),

    # Episode list of one show
    url(r'^(?P<slug>[-\w]+)/$', view='episode_list', name='podcast_episodes'),

    # Episode list feed by show (RSS 2.0 and iTunes)
    url(r'^(?P<slug>[-\w]+)/feed/$', view='show_list_feed', name='podcast_feed'),

    # Episode list feed by show (Atom)
    url(r'^(?P<slug>[-\w]+)/atom/$', view='show_list_feed', name='podcast_atom'),
    
    # Episode list feed by show (Media RSS)
    url(r'^(?P<slug>[-\w]+)/media/$', view='show_list_feed', name='podcast_media'),

    # Episode list feed by show (Photocast)
    url(r'^(?P<slug>[-\w]+)/photocast/$', view='show_list_feed', name='podcast_photo'),

    # Episode detail of one show
    url(r'^(?P<show_slug>[-\w]+)/(?P<episode_slug>[-\w]+)/$', view='episode_detail', name='podcast_episode'),

    # Episode sitemap list of one show
    url(r'^(?P<slug>[-\w]+)/sitemap.xml$', view='episode_sitemap', name='podcast_sitemap'),
)