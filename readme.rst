==============
django-podcast
==============

*django-podcast* is a Django application that allows you to easily publish podcasts that conform to the RSS 2.0 and iTunes RSS podcast specifications.

Django and Python version
=========================

django-podcast requires at least [http://code.djangoproject.com/changeset/7967 Django 0.97 revision 7967]. This revision incorporated the newforms-admin branch into trunk and makes the most notable use of it in the categories class of the application's models. However, I *heavily* encourage you to [http://www.djangoproject.com/download/ develop with the Django development version] (known as "trunk"), which is Django 1.0.x at the time of this writing. At the least, please use Django 1.0.

If you're developing on a web host, Python is probably already installed. To check, type ``python`` from the command line after logging in via SSH. If Python isn't installed, [http://www.python.org download and install Python]. At least Python version 2.3 is recommended.:

    ``ssh user@domain.com``
    
    ``python``

Installation
============

After connecting to your server via SSH, typically you download Django and other packages into a ``source`` directory. You would then symlink the ``django`` directory to a location that resides on your Python path. Likewise, download django-podcast from the Google Code Subversion repository and symlink the ``podcast`` directory.

If you work with WebFaction (like I do), and assuming one location on your Python path is ``$HOME/webapps/django/lib/python2.5``, it might go like::

    mkdir ~/source
    svn co http://code.djangoproject.com/svn/django/trunk/ $HOME/source/django-trunk/
    ln -s $HOME/source/django-trunk/django/ $HOME/webapps/django/lib/python2.5/django
    svn co http://django-podcast.googlecode.com/svn/trunk/ $HOME/source/django-podcast-read-only/
    ln -s $HOME/source/django-podcast-read-only/podcast/ $HOME/webapps/django/lib/python2.5/podcast

Add ``podcast`` as a tuple item to your ``INSTALLED_APPS`` in ``settings.py``::

    INSTALLED_APPS = (
      ...
      'podcast',
    )

Add these lines to your URL configuration, ``urls.py``::

    urlpatterns += patterns('', 
        (r'^podcasts/', include('podcast.urls')),
    )

Run the ``syncdb`` command from the directory in which your ``settings.py`` resides, most probably your applications' project directory. Again, if you're on WebFaction like I am, where ``example-project`` is your project name:

    cd ~/webapps/django/example-project/
    python manage.py syncdb

Alternatively if the Django binary directory is on your Python path, run the ``syncdb`` command from any directory to install the database tables.

    django-admin.py syncdb

If you installed the Django admin application, you should be able to see the podcast application's show and episode areas:

    http://www.example.com/admin/podcast/

You might need to restart the server for changes to take effect, especially if you are running Django on ``mod_python``.

Dependencies
============

None. However, consider a thumbnail creation utility, such as [http://code.google.com/p/sorl-thumbnail/ sorl-thumbnail], if you are not in control of creating your podcast show artwork. iTunes suggests show artwork should be a width and height of 600 pixels, but you might want to reduce the size of artwork on your website.

Web site URLs
=============

The default, out-of-the-box Web site URLs should look something like::

    http://www.example.com/podcasts/
    http://www.example.com/podcasts/title-of-show/
    http://www.example.com/podcasts/title-of-show/title-of-episode/

The ``/podcasts/`` portion of the URL is hard coded into the URL configuration. Beautifully designed default templates are included, so feel free to show off your URLs after saving a show and an episode! Note that the templates were not stress tested in Internet Explorer 6 or 7, but work on Web standards browsers.

FeedBurner and iTunes URLs
==========================

After saving at least one show and one episode, consider submitting your feed URL to [http://www.feedburner.com FeedBurner] for keeping track of podcast subscriber statistics. Your feed URL should be something like, where ``title-of-show`` is the slug of your show:

    http://www.example.com/podcasts/title-of-show/feed/

Remember to check the checkbox for "I'm a podcaster!" Your new FeedBurner URL should be something like:

    http://feeds.feedburner.com/TitleOfShow

You can now return to your website's admin and paste this URL into your Show's FeedBurner textbox. For bonus points, [https://phobos.apple.com/WebObjects/MZFinance.woa/wa/publishPodcast submit your FeedBurner URL to the iTunes Store]. Your iTunes podcast URL should then be something like::

    http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewPodcast?id=000000000

The advantage of submitting your FeedBurner URL to the iTunes Store allows you to track show statistics while also giving users the advantage of using the friendly iTunes interface. Return to the admin again and paste the iTunes show URL into the Show's iTunes URL textbox. Promote either the FeedBurner URL or the iTunes URL using each respective template tag on your website (in the simplest example)::

    {{ show.feedburner }}

    {{ show.itunes }}

Ping iTunes for new content
===========================

The iTunes Store checks new content daily but you might want to make a new episode available immediately in the iTunes Store. Visit your show's ping URL to make that episode available, which would be something like::

    https://phobos.apple.com/WebObjects/MZFinance.woa/wa/pingPodcast?id=000000000

Alternatively, if you're a savvy developer, you could set up a ``cron`` job to handle this, but note that pinging too often could result in a removal from the iTunes Store.

Yahoo! Media RSS feed submission
================================

Likewise, considering [http://search.yahoo.com/mrss/submit submitting your podcast to Yahoo! Search], which specifically accepts any kind of regularly published media-based (audio, video, image, document, etc.) RSS 2.0 feed or Media RSS feed.

Your Media RSS feed should be something like::

    http://www.example.com/podcasts/title-of-show/media/

Google video sitemaps
=====================

If you're creating a video podcast, you can [http://www.google.com/support/webmasters/bin/answer.py?answer=34575 submit a video sitemap] to [http://www.google.com/webmasters/tools/ Google Webmaster Tools]. The video sitemap will help Google index videos in [http://video.google.com Google Video].

After a successful installation, the video sitemap URL should be something like::

    http://www.example.com/podcasts/title-of-show/sitemap.xml

Additionally, you can [http://www.google.com/support/webmasters/bin/answer.py?answer=64748 add the video sitemap URL] to your robots.txt file.:

    Sitemap: http://www.example.com/podcasts/title-of-show/sitemap.xml

Google allows the submission of a media RSS feed instead of the sitemap to Google Webmaster Tools if you prefer.

Relevant links
==============

Some URLs that helped me and could help you:

Specifications
==============

- [http://cyber.law.harvard.edu/rss/rss.html RSS 2.0 specification]
- [http://www.apple.com/itunes/whatson/podcasts/specs.html Apple iTunes podcast technical specification]
- [http://search.yahoo.com/mrss Media RSS 2.0 Module specification]
- [http://www.google.com/webmasters/tools/video/en/video.html Google Video Media RSS Specification]
- [http://www.atomenabled.org/developers/syndication/atom-format-spec.php Atom syndication format specification]
- [http://www.google.com/support/webmasters/bin/topic.py?topic=10079 Google video sitemaps]

Tutorials, Validators, Software
===============================

- Comparing Media RSS formats: http://www.w3.org/2005/07/media-and-rss.html
- Webmonkey's "Use Media RSS": http://www.webmonkey.com/tutorial/Use_Media_RSS
- Apple iTunes podcasts: http://itunes.apple.com/WebObjects/MZStore.woa/wa/viewGenre?id=26
  - Apple iTunes audio podcasts: http://itunes.apple.com/WebObjects/MZStore.woa/wa/viewGrouping?id=25306&subMediaType=Audio
  - Apple iTunes video podcasts: http://itunes.apple.com/WebObjects/MZStore.woa/wa/viewGrouping?id=25314&subMediaType=Video
  - Apple iTunes HD podcasts: http://itunes.apple.com/WebObjects/MZStore.woa/wa/viewRoom?fcId=258879357&id=20814
- Feed Validator: http://www.feedvalidator.org
- MetaX, Macintosh meta-data tagger (for saving episode-specific artwork and other meta data): http://www.kerstetter.net/page53/page54/page54.html

For the curious, django-podcast is compatible with [http://en.wikipedia.org/wiki/Enhanced_podcast enhanced podcasts] and HD podcasts; both depend on the respective file's preparation and not on the feeds.

Licensing
=========

This software is licensed under the [http://en.wikipedia.org/wiki/BSD_license new BSD license].

Support
=======

Please [http://code.google.com/p/django-podcast/issues/list file a ticket if you find a problem with this application], and if you're feeling generous a patch to go with it. Help me help you!

If you used this Django application, I'd love to see it in action, and if you have suggestions or feature requests, drop me a line at rich (at) richardcornish (dot) com and let me know.