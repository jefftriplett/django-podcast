from django.views.generic.list_detail import object_detail, object_list
from podcast.models import Episode, Show, Enclosure


def episode_detail(request, show_slug, episode_slug):
    """
    Episode detail

    Template:  ``podcast/episode_detail.html``
    Context:
        object_detail
            Detail of episode.
    """
    return object_detail(
        request=request,
        queryset=Episode.objects.published().filter(show__slug__exact=show_slug),
        slug=episode_slug,
        slug_field='slug',
        extra_context={
            'enclosure_list': Enclosure.objects.filter(episode__show__slug__exact=show_slug).filter(episode__slug__exact=episode_slug).order_by('-episode__date')},
        template_name='podcast/episode_detail.html')


def episode_list(request, slug):
    """
    Episode list

    Template:  ``podcast/episode_list.html``
    Context:
        object_list
            List of episodes.
    """
    return object_detail(
        request=request,
        queryset=Show.objects.all(),
        slug_field='slug',
        slug=slug,
        extra_context={
            'object_list': Episode.objects.published().filter(show__slug__exact=slug),
        },
        template_name='podcast/episode_list.html')


def episode_sitemap(request, slug):
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
        queryset=Episode.objects.published().filter(show__slug__exact=slug).order_by('-date'),
        extra_context={
            'enclosure_list': Enclosure.objects.filter(episode__show__slug__exact=slug).order_by('-episode__date')},
        template_name='podcast/episode_sitemap.html')


def show_list(request, slug=None, template_name='podcast/show_list.html', page=0, paginate_by=25, mimetype=None):
    """
    Episode list
    - feed by show

    Template:  ``podcast/show_list.html``
    Context:
        object_list
            List of shows.
    """

    if slug:
        shows = Show.objects.filter(slug__exact=slug)
    else:
        shows = Show.objects.all()

    return object_list(
        request=request,
        queryset=shows,
        template_name=template_name,
        paginate_by=paginate_by,
        page=page)


def show_list_atom(request, slug, template_name='podcast/show_feed_atom.html'):
    """
    Episode Atom feed for a given show

    Template:  ``podcast/show_feed_atom.html``
    Context:
        object
            Story detail
    """
    return object_detail(request,
        queryset=Show.objects.all(),
        mimetype='application/rss+xml',
        slug_field='slug',
        slug=slug,
        template_name=template_name)


def show_list_feed(request, slug, template_name='podcast/show_feed.html'):
    """
    Episode RSS feed for a given show

    Template:  ``podcast/show_feed.html``
    Context:
        object
            Story detail
    """
    return object_detail(request,
        queryset=Show.objects.all(),
        mimetype='application/rss+xml',
        slug_field='slug',
        slug=slug,
        template_name=template_name)


def show_list_media(request, slug, template_name='podcast/show_feed_media.html'):
    """
    Episode Media feed for a given show

    Template:  ``podcast/show_feed_media.html``
    Context:
        object
            Story detail
    """
    return object_detail(request,
        queryset=Show.objects.all(),
        mimetype='application/rss+xml',
        slug_field='slug',
        slug=slug,
        template_name=template_name)
