from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from podcast.models import Episode


def episode_detail(request, show_slug, episode_slug):
    """
    Episode detail

    Template:  ``podcast/episode_detail.html``
    Context:
        object_detail
            Detail of episode.
    """
    return object_detail(
        request,
        queryset=Episode.objects.published().filter(show__slug__exact=show_slug),
        slug=episode_slug,
        slug_field='slug',
        template_name='podcast/episode_detail.html')


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


def episode_list(request, slug):
    """
    Episode list

    Template:  ``podcast/episode_list.html``
    Context:
        object_list
            List of episodes.
    """
    return object_list(
        request,
        queryset=Episode.objects.published().filter(show__slug__exact=slug),
        template_name='podcast/episode_list.html')


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
