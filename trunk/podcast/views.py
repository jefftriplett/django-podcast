from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from podcast.models import *


def episode_feed(request):
    """
    Episode feed

    Template:  ``podcast/episode_feed.html``
    Context:
        object_list
            List of episodes.
    """
    return object_list(
        request,
        mimetype='application/rss+xml',
        queryset=Episode.objects.published(),
        template_name='podcast/episode_feed.html')


def episode_sitemap(request):
    """
    Episode sitemap

    Template:  ``podcast/episode_sitemap.html``
    Context:
        object_list
            List of episodes.
    """
    return object_list(
        request,
        mimetype='application/xml',
        queryset=Episode.objects.published(),
        template_name='podcast/episode_sitemap.html')
