from django.conf.urls.defaults import *


urlpatterns = patterns('podcast.views',
    # Podcast feed URL
    (r'^feedburner/$', 'episode_feed'),

    # Google Video sitemap
    (r'^sitemap.xml$', 'episode_sitemap'),
)