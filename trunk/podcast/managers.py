from django.db.models import Manager
import datetime


class EpisodeManager(Manager):
    """Returns public posts that are not in the future."""
    def __init__(self, *args, **kwargs):
        self.filter_dict = dict(status__exact=2, date__lte=datetime.datetime.now())
        super(EpisodeManager, self).__init__(*args, **kwargs)

    def published(self):
        return self.get_query_set().filter(**self.filter_dict)
