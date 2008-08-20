from django.db import models


class EpisodeManager(models.Manager):
    def __init__(self, *args, **kwargs):
        super(EpisodeManager, self).__init__(*args, **kwargs)

    def published(self):
        return self.get_query_set().filter(published=True)
