from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from podcast.models import *

def episode_feed(request):
    queryset = Episode.objects.published()
    template_object_name = 'episode'
    template_name = 'templates/episode_feed.html'
    return object_list(request, queryset=queryset, template_object_name=template_object_name, template_name=template_name)

def episode_sitemap(request):
    queryset = Episode.objects.published()
    template_object_name = 'episode'
    template_name = 'templates/episode_sitemap.html'
    extra_context = { 'episode_list': Episode.objects.published(), }
    return object_list(request, queryset=queryset, template_object_name=template_object_name, template_name=template_name)
