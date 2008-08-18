= django-podcast =

*django-podcast* is a Django application that allows you to easily publish podcasts that conform to the RSS 2.0 and iTunes RSS podcast specification.

*Currently migrating application to the newforms-admin trunk changes. Application will not work until migration is complete. Thanks for your patience.*

== Django and Python version ==

django-podcast requires at least [http://code.djangoproject.com/changeset/7967 Django 0.97 revision 7967]. This revision incorporated the newforms-admin branch into trunk and makes the most notable use of it in the categories class of the application's models. The Subversion command would be:

    `svn co http://code.djangoproject.com/svn/django/trunk/ django-trunk -r7967`

If you're developing on a web host, Python is probably already installed. To check, type `python` from the command line after logging in via SSH. If Python isn't installed, download Python 2.3 from http://www.python.org.

== Installation ==

Check out django-podcast from the Google Code Subversion repository. Typically, you could download it into a `source` packages directory, and then symlink the `podcast` directory to a location that resides on your Python path.

    `svn co http://django-podcast.googlecode.com/svn/trunk/ $HOME/source/django-podcast-read-only`
    
    `ln -s $HOME/source/django-podcast-read-only/podcast/ $HOME/lib/python/podcast`
    
You could simply physically move the "podcast" directory to a location that resides on your Python path, but that would break future Subversion updates.

Add `podcast` as a tuple item to your `INSTALLED_APPS` in `settings.py`:

    {{{
    INSTALLED_APPS = (
      ...
      'podcast',
      ...
    )
    }}}

Add these lines to your URL configuration, urls.py, replacing the `MyAwesomePodcast` as necessary (further instruction about FeedBurner below):

    {{{
    (r'^podcasts/$', include('podcast.urls')),
    (r'^podcasts/feed/$', 'django.views.generic.simple.redirect_to', {'url': 'http://feeds.feedburner.com/MyAwesomePodcast'}),
    }}}
    
Restart your server for the changes to take effect.

Assuming the Django binary directory is on your Python path, run the syncdb command to install the application's database tables.

    `django-admin.py syncdb`

If you installed the Django admin application, you should be able to see the podcast application's show and episode areas:

  * http://www.example.com/admin/podcast/show/
  * http://www.example.com/admin/podcast/episode/

== Dependencies ==

None. However, consider a thumbnail creation utility, such as [http://code.google.com/p/sorl-thumbnail/ sorl-thumbnail], if you are not in control of creating your podcast show album artwork. The album artwork must be a maximum width of 600 pixels.

== FeedBurner feed statistics ==

After installing django-podcast and saving a podcast show and episode, you don't need to do anything more to get your podcast going. However, consider integrating FeedBurner to track podcast feed statistics. The following process creates a "friendly" URL and an iTunes Store URL that both point to your FeedBurner URL, which ultimately looks to your original feed URL.

1. Create original feed URL for FeedBurner
   * http://www.example.com/podcasts/feedburner/
2. Submit URL to FeedBurner (check box for podcast)
   * http://www.feedburner.com/
3. Copy new FeedBurner URL to clipboard
   * http://feeds.feedburner.com/ExamplePodcast
4. Create "friendly" URL for a redirect
   * http://www.example.com/podcasts/feed/ -> http://feeds.feedburner.com/ExamplePodcast
5. Submit "friendly" URL to the iTunes Store
   * https://phobos.apple.com/WebObjects/MZFinance.woa/wa/publishPodcast
6. Promote either "friendly" URL or iTunes URL
   * http://www.example.com/podcasts/feed/
   * http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewPodcast?id=[Example iTunes Podcast ID] ... or
   * http://www.itunes.com/podcast?id=[Example iTunes Podcast ID]

Hat tip goes to [http://www.jeffcroft.com Jeff Croft] from whom I saw a variation on this trick in his [http://jeffcroft.com/blog/2007/may/28/lost-theoriescom-source-code-update/ Lost-Theories source code].

== Ping iTunes for new content ==

The iTunes Store checks new content daily but you might want to make sure a new episode is available immediately in the iTunes Store. Visit the ping URL to make that episode available: https://phobos.apple.com/WebObjects/MZFinance.woa/wa/pingPodcast?id=[Example iTunes Podcast ID]

Alternatively, if you're a savvy developer, you could set up a `cron` job to handle this, but pinging too often could result in a removal from the iTunes Store.

== Google video sitemaps ==

If you're creating a video podcast, you can submit a video sitemap to [http://www.google.com/webmasters/tools/ Google Webmaster Tools]. The video sitemap will help Google index videos in [http://video.google.com Google Video].

After a successful installation, the video sitemap URL should be available at http://www.example.com/podcasts/sitemap.xml.

== Relevant links ==

Some URLs that helped me and could help you:

 * [http://cyber.law.harvard.edu/rss/rss.html RSS 2.0 Specification]
 * [http://www.apple.com/itunes/store/podcaststechspecs.html Apple iTunes podcast technical specification]
 * [http://www.google.com/support/webmasters/bin/topic.py?topic=10079 Google video sitemaps]
 * [http://www.feedvalidator.org Feed Validator]
 * [http://www.kerstetter.net/page53/page54/page54.html MetaX, Macintosh meta-data tagger]
 * [http://www.techspansion.com/visualhub/ VisualHub]

== Licensing ==

This software is licensed under the [http://www.gnu.org/licenses/gpl-2.0.html GNU Public License v2].

== Support ==

 * [http://code.google.com/p/django-podcast/ Google Code project page]
 * [http://code.google.com/p/django-podcast/issues/ Questions and problems]

If you used this Django application, I'd love to see it in action. Or if you have suggestions or feature requests, drop me a line at rich (at) richardcornish (dot) com and let me know how you're using it or want to use it.