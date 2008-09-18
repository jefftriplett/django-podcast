from podcast.models import Organization, Category, Show, Episode
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'published')
    prepopulated_fields = {'slug': ("title",)}


class ShowAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ("title",)}


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Show, ShowAdmin)
