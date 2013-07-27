from django.views.generic import DetailView, ListView

from .models import Enclosure, Episode, Show


class EpisodeDetail(DetailView):
    model = Episode
    slug_url_kwarg = "episode_slug"

    def get_queryset(self):
        return self.model.objects.published().filter(show__slug__exact=self.kwargs['show_slug'])

    def get_context_data(self, **kwargs):
        context = super(EpisodeDetail, self).get_context_data(**kwargs)
        context['enclosure_list'] = Enclosure.objects.filter(episode__show__slug__exact=self.kwargs['show_slug']).filter(episode=self.object).order_by("-episode__date")
        return context

episode_detail = EpisodeDetail.as_view()


class EpisodeList(ListView):
    model = Episode

    def get_queryset(self):
        return self.model.objects.published().filter(show__slug__exact=self.kwargs['slug']).order_by('-date')

episode_list = EpisodeList.as_view()


class EpisodeSitemap(EpisodeList):
    template_name = 'podcast/episode_sitemap.html'
    content_type = 'application/xml'

    def get_context_data(self, **kwargs):
        context = super(EpisodeDetail, self).get_context_data(**kwargs)
        context['enclosure_list'] = Enclosure.objects.filter(episode__show__slug__exact=self.kwargs['slug']).order_by("-episode__date")
        return context

episode_sitemap = EpisodeSitemap.as_view()


class ShowList(ListView):
    model = Show
    paginate_by = 25

    def get_queryset(self):
        if self.kwargs.get("slug"):
            return self.model.objects.filter(slug__exact=self.kwargs['slug'])
        return self.model.objects.all()

show_list = ShowList.as_view()


class ShowListAtom(DetailView):
    model = Show
    template_name = 'podcast/show_feed_atom.html'
    content_type = 'application/rss+xml'

show_list_atom = ShowListAtom.as_view()


class ShowListFeed(ShowListAtom):
    template_name = 'podcast/show_feed.html'

show_list_feed = ShowListFeed.as_view()


class ShowListMedia(ShowListAtom):
    template_name = 'podcast/show_feed_media.html'

show_list_media = ShowListMedia.as_view()
