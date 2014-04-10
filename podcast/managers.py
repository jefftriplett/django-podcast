from django.db.models import Manager
from django.db.models.query import QuerySet
from django.utils import timezone


class EpisodeQuerySet(QuerySet):
    def draft(self):
        return self.filter(status__exact=self.model.STATUS_DRAFT)

    def private(self):
        return self.filter(status__exact=self.model.STATUS_DRAFT)

    def public(self):
        return self.filter(status__exact=self.model.STATUS_PUBLIC)

    def published(self):
        return self.filter(status__exact=self.model.STATUS_PUBLIC, date__lte=timezone.now())


class EpisodeManager(Manager):
    def get_query_set(self):
        return EpisodeQuerySet(self.model, using=self._db)

    def draft(self):
        return self.get_query_set().draft()

    def private(self):
        return self.get_query_set().private()

    def public(self):
        return self.get_query_set().public()

    def published(self):
        return self.get_query_set().published()
