from django.test import TestCase

from ..models import ParentCategory, ChildCategory, Show, MediaCategory, Episode, Enclosure


class PodcastTestCase(TestCase):
    urls = 'podcast.urls'

    def setUp(self):
        self.parent_category = ParentCategory()
        self.child_category = ChildCategory()
        self.show = Show()
        self.media_category = MediaCategory()
        self.episode = Episode()
        self.enclosure = Enclosure()

    def test_podcast_shows(self):
        self.assertTrue(True)

    def test_podcast_show_detail(self):
        self.assertTrue(True)

    def test_podcast_show_feed(self):
        self.assertTrue(True)

    def test_podcast_show_feed_atom(self):
        self.assertTrue(True)

    def test_podcast_show_feed_media_rss(self):
        self.assertTrue(True)

    def test_podcast_show_sitemap(self):
        self.assertTrue(True)

    def test_podcast_episode_detail(self):
        self.assertTrue(True)
