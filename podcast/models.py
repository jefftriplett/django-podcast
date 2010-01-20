from django.db import models
from django.contrib.auth.models import User
from podcast.managers import EpisodeManager


class ParentCategory(models.Model):
    """Parent Category model."""
    PARENT_CHOICES = (
        ('Arts', 'Arts'),
        ('Business', 'Business'),
        ('Comedy', 'Comedy'),
        ('Education', 'Education'),
        ('Games & Hobbies', 'Games & Hobbies'),
        ('Government & Organizations', 'Government & Organizations'),
        ('Health', 'Health'),
        ('Kids & Family', 'Kids & Family'),
        ('Music', 'Music'),
        ('News & Politics', 'News & Politics'),
        ('Religion & Spirituality', 'Religion & Spirituality'),
        ('Science & Medicine', 'Science & Medicine'),
        ('Society & Culture', 'Society & Culture'),
        ('Sports & Recreation', 'Sports & Recreation'),
        ('Technology', 'Technology'),
        ('TV & Film', 'TV & Film'),
    )
    name = models.CharField(max_length=50, choices=PARENT_CHOICES, help_text='After saving this parent category, please map it to one or more Child Categories below.')
    slug = models.SlugField(blank=True, unique=False, help_text='A <a href="http://docs.djangoproject.com/en/dev/ref/models/fields/#slugfield">slug</a> is a URL-friendly nickname. For example, a slug for "Games & Hobbies" is "games-hobbies".')

    class Meta:
        ordering = ['slug']
        verbose_name = 'category (iTunes parent)'
        verbose_name_plural = 'categories (iTunes parent)'

    def __unicode__(self):
        return u'%s' % (self.name)


class ChildCategory(models.Model):
    """Child Category model."""
    CHILD_CHOICES = (
        ('Arts', (
                ('Design', 'Design'),
                ('Fashion & Beauty', 'Fashion & Beauty'),
                ('Food', 'Food'),
                ('Literature', 'Literature'),
                ('Performing Arts', 'Performing Arts'),
                ('Visual Arts', 'Visual Arts'),
            )
        ),
        ('Business', (
                ('Business News', 'Business News'),
                ('Careers', 'Careers'),
                ('Investing', 'Investing'),
                ('Management & Marketing', 'Management & Marketing'),
                ('Shopping', 'Shopping'),
            )
        ),
        ('Education', (
                ('Education Technology', 'Education Technology'),
                ('Higher Education', 'Higher Education'),
                ('K-12', 'K-12'),
                ('Language Courses', 'Language Courses'),
                ('Training', 'Training'),
            )
        ),
        ('Games & Hobbies', (
                ('Automotive', 'Automotive'),
                ('Aviation', 'Aviation'),
                ('Hobbies', 'Hobbies'),
                ('Other Games', 'Other Games'),
                ('Video Games', 'Video Games'),
            )
        ),
        ('Government & Organizations', (
                ('Local', 'Local'),
                ('National', 'National'),
                ('Non-Profit', 'Non-Profit'),
                ('Regional', 'Regional'),
            )
        ),
        ('Health', (
                ('Alternative Health', 'Alternative Health'),
                ('Fitness & Nutrition', 'Fitness & Nutrition'),
                ('Self-Help', 'Self-Help'),
                ('Sexuality', 'Sexuality'),
            )
        ),
        ('Religion & Spirituality', (
                ('Buddhism', 'Buddhism'),
                ('Christianity', 'Christianity'),
                ('Hinduism', 'Hinduism'),
                ('Islam', 'Islam'),
                ('Judaism', 'Judaism'),
                ('Other', 'Other'),
                ('Spirituality', 'Spirituality'),
            )
        ),
        ('Science & Medicine', (
                ('Medicine', 'Medicine'),
                ('Natural Sciences', 'Natural Sciences'),
                ('Social Sciences', 'Social Sciences'),
            )
        ),
        ('Society & Culture', (
                ('History', 'History'),
                ('Personal Journals', 'Personal Journals'),
                ('Philosophy', 'Philosophy'),
                ('Places & Travel', 'Places & Travel'),
            )
        ),
        ('Sports & Recreation', (
                ('Amateur', 'Amateur'),
                ('College & High School', 'College & High School'),
                ('Outdoor', 'Outdoor'),
                ('Professional', 'Professional'),
            )
        ),
        ('Technology', (
                ('Gadgets', 'Gadgets'),
                ('Tech News', 'Tech News'),
                ('Podcasting', 'Podcasting'),
                ('Software How-To', 'Software How-To'),
            )
        ),
    )
    parent = models.ForeignKey(ParentCategory, related_name='child_category_parents')
    name = models.CharField(max_length=50, blank=True, choices=CHILD_CHOICES, help_text='Please choose a child category that corresponds to its respective parent category (e.g., "Design" is a child category of "Arts").<br />If no such child category exists for a parent category (e.g., Comedy, Kids & Family, Music, News & Politics, or TV & Film), simply leave this blank and save.')
    slug = models.SlugField(blank=True, unique=False, help_text='A <a href="http://docs.djangoproject.com/en/dev/ref/models/fields/#slugfield">slug</a> is a URL-friendly nickname. For exmaple, a slug for "Fashion & Beauty" is "fashion-beauty".')

    class Meta:
        ordering = ['parent', 'slug']
        verbose_name = 'category (iTunes child)'
        verbose_name_plural = 'categories (iTunes child)'

    def __unicode__(self):
        if self.name!='':
            return u'%s > %s' % (self.parent, self.name)
        else:
            return u'%s' % (self.parent)


class Show(models.Model):
    """Show model."""
    COPYRIGHT_CHOICES = (
        ('All rights reserved', 'All rights reserved'),
        ('Creative Commons: Attribution (by)', 'Creative Commons: Attribution (by)'),
        ('Creative Commons: Attribution-Share Alike (by-sa)', 'Creative Commons: Attribution-Share Alike (by-sa)'),
        ('Creative Commons: Attribution-No Derivatives (by-nd)', 'Creative Commons: Attribution-No Derivatives (by-nd)'),
        ('Creative Commons: Attribution-Non-Commercial (by-nc)', 'Creative Commons: Attribution-Non-Commercial (by-nc)'),
        ('Creative Commons: Attribution-Non-Commercial-Share Alike (by-nc-sa)', 'Creative Commons: Attribution-Non-Commercial-Share Alike (by-nc-sa)'),
        ('Creative Commons: Attribution-Non-Commercial-No Dreivatives (by-nc-nd)', 'Creative Commons: Attribution-Non-Commercial-No Dreivatives (by-nc-nd)'),
        ('Public domain', 'Public domain'),
    )
    EXPLICIT_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Clean', 'Clean'),
    )
    # RSS 2.0
    organization = models.CharField(max_length=255, help_text='Name of the organization, company or Web site producing the podcast.')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, help_text='Auto-generated from Title.')
    link = models.URLField(help_text='URL of either the main website or the podcast section of the main website.')
    description = models.TextField(help_text='Describe subject matter, media format, episode schedule and other relevant information while incorporating keywords.')
    language = models.CharField(max_length=5, default='en-us', help_text='Default is American English. See <a href="http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">ISO 639-1</a> and <a href="http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements">ISO 3166-1</a> for more language codes.', blank=True)
    copyright = models.CharField(max_length=255, default='All rights reserved', choices=COPYRIGHT_CHOICES, help_text='See <a href="http://creativecommons.org/about/license/">Creative Commons licenses</a> for more information.')
    copyright_url = models.URLField('Copyright URL', blank=True, help_text='A URL pointing to additional copyright information. Consider a <a href="http://creativecommons.org/licenses/">Creative Commons license URL</a>.')
    author = models.ManyToManyField(User, related_name='show_authors', help_text='Remember to save the user\'s name and e-mail address in the <a href="../../../auth/user/">User application</a>.<br />')
    webmaster = models.ForeignKey(User, related_name='webmaster', blank=True, null=True, help_text='Remember to save the user\'s name and e-mail address in the <a href="../../../auth/user/">User application</a>.')
    category_show = models.CharField('Category', max_length=255, blank=True, help_text='Limited to one user-specified category for the sake of sanity.')
    domain = models.URLField(blank=True, help_text='A URL that identifies a categorization taxonomy.')
    ttl = models.PositiveIntegerField('TTL', help_text='"Time to Live," the number of minutes a channel can be cached before refreshing.', blank=True, null=True)
    image = models.ImageField(upload_to='podcasts/shows/img/', help_text='An attractive, original square JPEG (.jpg) or PNG (.png) image of 600x600 pixels. Image will be scaled down to 50x50 pixels at smallest in iTunes.', blank=True)
    feedburner = models.URLField('FeedBurner URL', help_text='Fill this out after saving this show and at least one episode. URL should look like "http://feeds.feedburner.com/TitleOfShow". See <a href="http://code.google.com/p/django-podcast/">documentation</a> for more.', blank=True)
    # iTunes
    subtitle = models.CharField(max_length=255, help_text='Looks best if only a few words, like a tagline.', blank=True)
    summary = models.TextField(help_text='Allows 4,000 characters. Description will be used if summary is blank.', blank=True)
    category = models.ManyToManyField(ChildCategory, related_name='show_categories', help_text='If selecting a category group with no child category (e.g., Comedy, Kids & Family, Music, News & Politics or TV & Film), save that parent category with a blank <a href="../../childcategory/">child category</a>.<br />Selecting multiple category groups makes the podcast more likely to be found by users.<br />', blank=True)
    explicit = models.CharField(max_length=255, default='No', choices=EXPLICIT_CHOICES, help_text='"Clean" will put the clean iTunes graphic by it.', blank=True)
    block = models.BooleanField(default=False, help_text='Check to block this show from iTunes. <br />Show will remain blocked until unchecked.')
    redirect = models.URLField(help_text='The show\'s new URL feed if changing the URL of the current show feed. Must continue old feed for at least two weeks and write a 301 redirect for old feed.', blank=True)
    keywords = models.CharField(max_length=255, help_text='A comma-demlimited list of up to 12 words for iTunes searches. Perhaps include misspellings of the title.', blank=True)
    itunes = models.URLField('iTunes Store URL', help_text='Fill this out after saving this show and at least one episode. URL should look like "http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewPodcast?id=000000000". See <a href="http://code.google.com/p/django-podcast/">documentation</a> for more.', blank=True)

    class Meta:
        ordering = ['organization', 'slug']

    def __unicode__(self):
        return u'%s' % (self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('podcast_episodes', (), {'slug': self.slug})


class MediaCategory(models.Model):
    """Category model for Media RSS"""
    MEDIA_CATEGORY_CHOICES = (
        ('Action & Adventure', 'Action & Adventure'),
        ('Ads & Promotional', 'Ads & Promotional'),
        ('Anime & Animation', 'Anime & Animation'),
        ('Art & Experimental', 'Art & Experimental'),
        ('Business', 'Business'),
        ('Children & Family', 'Children & Family'),
        ('Comedy', 'Comedy'),
        ('Dance', 'Dance'),
        ('Documentary', 'Documentary'),
        ('Drama', 'Drama'),
        ('Educational', 'Educational'),
        ('Faith & Spirituality', 'Faith & Spirituality'),
        ('Health & Fitness', 'Health & Fitness'),
        ('Foreign', 'Foreign'),
        ('Gaming', 'Gaming'),
        ('Gay & Lesbian', 'Gay & Lesbian'),
        ('Home Video', 'Home Video'),
        ('Horror', 'Horror'),
        ('Independent', 'Independent'),
        ('Mature & Adult', 'Mature & Adult'),
        ('Movie (feature)', 'Movie (feature)'),
        ('Movie (short)', 'Movie (short)'),
        ('Movie Trailer', 'Movie Trailer'),
        ('Music & Musical', 'Music & Musical'),
        ('Nature', 'Nature'),
        ('News', 'News'),
        ('Political', 'Political'),
        ('Religious', 'Religious'),
        ('Romance', 'Romance'),
        ('Independent', 'Independent'),
        ('Sci-Fi & Fantasy', 'Sci-Fi & Fantasy'),
        ('Science & Technology', 'Science & Technology'),
        ('Special Interest', 'Special Interest'),
        ('Sports', 'Sports'),
        ('Stock Footage', 'Stock Footage'),
        ('Thriller', 'Thriller'),
        ('Travel', 'Travel'),
        ('TV Show', 'TV Show'),
        ('Western', 'Western'),
    )
    name = models.CharField(max_length=50, choices=MEDIA_CATEGORY_CHOICES)
    slug = models.SlugField(blank=True, unique=False, help_text='A <a href="http://docs.djangoproject.com/en/dev/ref/models/fields/#slugfield">slug</a> is a URL-friendly nickname. For example, a slug for "Games & Hobbies" is "games-hobbies".')

    class Meta:
        ordering = ['slug']
        verbose_name = 'category (Media RSS)'
        verbose_name_plural = 'categories (Media RSS)'

    def __unicode__(self):
        return u'%s' % (self.name)


class Episode(models.Model):
    """Episode model."""
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Public'),
        (3, 'Private'),
    )
    SECONDS_CHOICES = tuple(('%02d' % x, str(x)) for x in range(60))
    EXPLICIT_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Clean', 'Clean'),
    )
    TYPE_CHOICES = (
        ('Plain', 'Plain text'),
        ('HTML', 'HTML'),
    )
    ROLE_CHOICES = (
        ('Actor', 'Actor'),
        ('Adaptor', 'Adaptor'),
        ('Anchor person', 'Anchor person'),
        ('Animal Trainer', 'Animal Trainer'),
        ('Animator', 'Animator'),
        ('Announcer', 'Announcer'),
        ('Armourer', 'Armourer'),
        ('Art Director', 'Art Director'),
        ('Artist/Performer', 'Artist/Performer'),
        ('Assistant Camera', 'Assistant Camera'),
        ('Assistant Chief Lighting Technician', 'Assistant Chief Lighting Technician'),
        ('Assistant Director', 'Assistant Director'),
        ('Assistant Producer', 'Assistant Producer'),
        ('Assistant Visual Editor', 'Assistant Visual Editor'),
        ('Author', 'Author'),
        ('Broadcast Assistant', 'Broadcast Assistant'),
        ('Broadcast Journalist', 'Broadcast Journalist'),
        ('Camera Operator', 'Camera Operator'),
        ('Carpenter', 'Carpenter'),
        ('Casting', 'Casting'),
        ('Causeur', 'Causeur'),
        ('Chief Lighting Technician', 'Chief Lighting Technician'),
        ('Choir', 'Choir'),
        ('Choreographer', 'Choreographer'),
        ('Clapper Loader', 'Clapper Loader'),
        ('Commentary or Commentator', 'Commentary or Commentator'),
        ('Commissioning Broadcaster', 'Commissioning Broadcaster'),
        ('Composer', 'Composer'),
        ('Computer programmer', 'Computer programmer'),
        ('Conductor', 'Conductor'),
        ('Consultant', 'Consultant'),
        ('Continuity Checker', 'Continuity Checker'),
        ('Correspondent', 'Correspondent'),
        ('Costume Designer', 'Costume Designer'),
        ('Dancer', 'Dancer'),
        ('Dialogue Coach', 'Dialogue Coach'),
        ('Director', 'Director'),
        ('Director of Photography', 'Director of Photography'),
        ('Distribution Company', 'Distribution Company'),
        ('Draughtsman', 'Draughtsman'),
        ('Dresser', 'Dresser'),
        ('Dubber', 'Dubber'),
        ('Editor/Producer (News)', 'Editor/Producer (News)'),
        ('Editor-in-chief', 'Editor-in-chief'),
        ('Editor-of-the-Day', 'Editor-of-the-Day'),
        ('Ensemble', 'Ensemble'),
        ('Executive Producer', 'Executive Producer'),
        ('Expert', 'Expert'),
        ('Fight Director', 'Floor Manager'),
        ('Floor Manager', 'Floor Manager'),
        ('Focus Puller', 'Focus Puller'),
        ('Foley Artist', 'Foley Artist'),
        ('Foley Editor', 'Foley Editor'),
        ('Foley Mixer', 'Foley Mixer'),
        ('Graphic Assistant', 'Graphic Assistant'),
        ('Graphic Designer', 'Graphic Designer'),
        ('Greensman', 'Greensman'),
        ('Grip', 'Grip'),
        ('Hairdresser', 'Hairdresser'),
        ('Illustrator', 'Illustrator'),
        ('Interviewed Guest', 'Interviewed Guest'),
        ('Interviewer', 'Interviewer'),
        ('Key Character', 'Key Character'),
        ('Key Grip', 'Key Grip'),
        ('Key Talents', 'Key Talents'),
        ('Leadman', 'Leadman'),
        ('Librettist', 'Librettist'),
        ('Lighting director', 'Lighting director'),
        ('Lighting Technician', 'Lighting Technician'),
        ('Location Manager', 'Location Manager'),
        ('Lyricist', 'Lyricist'),
        ('Make Up Artist', 'Make Up Artist'),
        ('Manufacturer', 'Manufacturer'),
        ('Matte Artist', 'Matte Artist'),
        ('Music Arranger', 'Music Arranger'),
        ('Music Group', 'Music Group'),
        ('Musician', 'Musician'),
        ('News Reader', 'News Reader'),
        ('Orchestra', 'Orchestra'),
        ('Participant', 'Participant'),
        ('Photographer', 'Photographer'),
        ('Post-Production Editor', 'Post-Production Editor'),
        ('Producer', 'Producer'),
        ('Production Assistant', 'Production Assistant'),
        ('Production Company', 'Production Company'),
        ('Production Department', 'Production Department'),
        ('Production Manager', 'Production Manager'),
        ('Production Secretary', 'Production Secretary'),
        ('Programme Production Researcher', 'Programme Production Researcher'),
        ('Property Manager', 'Property Manager'),
        ('Publishing Company', 'Publishing Company'),
        ('Puppeteer', 'Puppeteer'),
        ('Pyrotechnician', 'Pyrotechnician'),
        ('Reporter', 'Reporter'),
        ('Rigger', 'Rigger'),
        ('Runner', 'Runner'),
        ('Scenario', 'Scenario'),
        ('Scenic Operative', 'Scenic Operative'),
        ('Script Supervisor', 'Script Supervisor'),
        ('Second Assistant Camera', 'Second Assistant Camera'),
        ('Second Assistant Director', 'Second Assistant Director'),
        ('Second Unit Director', 'Second Unit Director'),
        ('Set Designer', 'Set Designer'),
        ('Set Dresser', 'Set Dresser'),
        ('Sign Language', 'Sign Language'),
        ('Singer', 'Singer'),
        ('Sound Designer', 'Sound Designer'),
        ('Sound Mixer', 'Sound Mixer'),
        ('Sound Recordist', 'Sound Recordist'),
        ('Special Effects', 'Special Effects'),
        ('Stunts', 'Stunts'),
        ('Subtitles', 'Subtitles'),
        ('Technical Director', 'Technical Director'),
        ('Translation', 'Translation'),
        ('Transportation Manager', 'Transportation Manager'),
        ('Treatment / Programme Proposal', 'Treatment / Programme Proposal'),
        ('Vision Mixer', 'Vision Mixer'),
        ('Visual Editor', 'Visual Editor'),
        ('Visual Effects', 'Visual Effects'),
        ('Wardrobe', 'Wardrobe'),
        ('Witness', 'Witness'),
    )
    STANDARD_CHOICES = (
        ('Simple', 'Simple'),
        ('MPAA', 'MPAA'),
        ('V-chip', 'TV Parental Guidelines'),
    )
    RATING_CHOICES = (
        ('Simple', (
                ('Adult', 'Adult'),
                ('Nonadult', 'Non-adult'),
            )
        ),
        ('MPAA', (
                ('G', 'G: General Audiences'),
                ('PG', 'PG: Parental Guidance Suggested'),
                ('PG-13', 'PG-13: Parents Strongly Cautioned'),
                ('R', 'R: Restricted'),
                ('NC-17', 'NC-17: No One 17 and Under Admitted'),
            )
        ),
        ('TV Parental Guidelines', (
                ('TV-Y', 'TV-Y: All children'),
                ('TV-Y7-FV', 'TV-Y7/TV-Y7-FV: Directed to older children'),
                ('TV-G', 'TV-G: General audience'),
                ('TV-PG', 'TV-PG: Parental guidance'),
                ('TV-14', 'TV-14: Parents strongly cautioned'),
                ('TV-MA', 'TV-MA: Mature audiences'),
            )
        ),
    )
    FREQUENCY_CHOICES = (
        ('always', 'Always'),
        ('hourly', 'Hourly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('never', 'Never'),
    )
    # RSS 2.0
    show = models.ForeignKey(Show)
    author = models.ManyToManyField(User, related_name='episode_authors', help_text='Remember to save the user\'s name and e-mail address in the <a href="../../../auth/user/">User application</a>.')
    title_type = models.CharField('Title type', max_length=255, blank=True, default='Plain', choices=TYPE_CHOICES)
    title = models.CharField(max_length=255, help_text='Make it specific but avoid explicit language. Limit to 100 characters for a Google video sitemap.')
    slug = models.SlugField(unique=True, help_text='Auto-generated from Title.')
    description_type = models.CharField('Description type', max_length=255, blank=True, default='Plain', choices=TYPE_CHOICES)
    description = models.TextField(help_text='Avoid explicit language. Google video sitempas allow 2,048 characters.')
    captions = models.FileField(upload_to='podcasts/episodes/captions/', help_text='For video podcasts. Good captioning choices include <a href="http://en.wikipedia.org/wiki/SubViewer">SubViewer</a>, <a href="http://en.wikipedia.org/wiki/SubRip">SubRip</a> or <a href="http://www.w3.org/TR/ttaf1-dfxp/">TimedText</a>.', blank=True)
    category = models.CharField(max_length=255, blank=True, help_text='Limited to one user-specified category for the sake of sanity.')
    domain = models.URLField(blank=True, help_text='A URL that identifies a categorization taxonomy.')
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, blank=True, help_text='The frequency with which the episode\'s data changes. For sitemaps.', default='never')
    priority = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, help_text='The relative priority of this episode compared to others. 1.0 is the most important. For sitemaps.', default='0.5')
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # iTunes
    subtitle = models.CharField(max_length=255, help_text='Looks best if only a few words like a tagline.', blank=True)
    summary = models.TextField(help_text='Allows 4,000 characters. Description will be used if summary is blank.', blank=True)
    minutes = models.PositiveIntegerField(blank=True, null=True)
    seconds = models.CharField(max_length=2, blank=True, null=True, choices=SECONDS_CHOICES)
    keywords = models.CharField(max_length=255, help_text='A comma-delimited list of words for searches, up to 12; perhaps include misspellings.', blank=True, null=True)
    explicit = models.CharField(max_length=255, choices=EXPLICIT_CHOICES, help_text='"Clean" will put the clean iTunes graphic by it.', default='No')
    block = models.BooleanField(help_text='Check to block this episode from iTunes because <br />its content might cause the entire show to be <br />removed from iTunes.', default=False)
    # Media RSS
    role = models.CharField(max_length=255, blank=True, choices=ROLE_CHOICES, help_text='Role codes provided by the <a href="http://www.ebu.ch/en/technical/metadata/specifications/role_codes.php">European Broadcasting Union</a>.')
    media_category = models.ManyToManyField(MediaCategory, related_name='episode_categories', blank=True)
    standard = models.CharField(max_length=255, blank=True, choices=STANDARD_CHOICES, default='Simple')
    rating = models.CharField(max_length=255, blank=True, choices=RATING_CHOICES, help_text='If used, selection must match respective Scheme selection.', default='Nonadult')
    image = models.ImageField(upload_to='podcasts/episodes/img/', help_text='A still image from a video file, but for episode artwork to display in iTunes, image must be <a href="http://answers.yahoo.com/question/index?qid=20080501164348AAjvBvQ">saved to file\'s <strong>metadata</strong></a> before episode uploading!', blank=True)
    text = models.TextField(blank=True, help_text='Media RSS text transcript. Must use <media:text> tags. Please see the <a href="https://www.google.com/webmasters/tools/video/en/video.html#tagMediaText">Media RSS 2.0</a> specification for syntax.')
    deny = models.BooleanField(default=False, help_text='Check to deny episode to be shown to users from specified countries.')
    restriction = models.CharField(max_length=255, blank=True, help_text='A space-delimited list of <a href="http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements">ISO 3166-1-coded countries</a>.')
    # Dublin Core
    start = models.DateTimeField(blank=True, null=True, help_text='Start date and time that the media is valid.')
    end = models.DateTimeField(blank=True, null=True, help_text='End date and time that the media is valid.')
    scheme = models.CharField(max_length=255, blank=True, default='W3C-DTF')
    name = models.CharField(max_length=255, blank=True, help_text='Any helper name to distinguish this time period.')
    # Google Media
    preview = models.BooleanField(default=False, help_text="Check to allow Google to show a preview of your media in search results.")
    preview_start_mins = models.PositiveIntegerField('Preview start (minutes)', blank=True, null=True, help_text='Start time (minutes) of the media\'s preview, <br />shown on Google.com search results before <br />clicking through to see full video.')
    preview_start_secs = models.CharField('Preview start (seconds)', max_length=2, blank=True, null=True, choices=SECONDS_CHOICES, help_text='Start time (seconds) of the media\'s preview.')
    preview_end_mins = models.PositiveIntegerField('Preview end (minutes)', blank=True, null=True, help_text='End time (minutes) of the media\'s preview, <br />shown on Google.com search results before <br />clicking through to see full video.')
    preview_end_secs = models.CharField('Preview end (seconds)', max_length=2, blank=True, null=True, choices=SECONDS_CHOICES, help_text='End time (seconds) of the media\'s preview.')
    host = models.BooleanField(default=False, help_text='Check to allow Google to host your media after it expires. Must set expiration date in Dublin Core.')
    # Behind the scenes
    objects = EpisodeManager()

    class Meta:
        ordering = ['-date', 'slug']

    def __unicode__(self):
        return u'%s' % (self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('podcast_episode', (), {'show_slug': self.show.slug, 'episode_slug': self.slug})

    def seconds_total(self):
        try:
            return (((float(self.minutes)) * 60) + (float(self.seconds)))
        except:
            return 0


class Enclosure(models.Model):
    """Enclosure model."""
    MIME_CHOICES = (
        ('audio/mpeg', '.mp3 (audio)'),
        ('audio/x-m4a', '.m4a (audio)'),
        ('video/mp4', '.mp4 (audio or video)'),
        ('video/x-m4v', '.m4v (video)'),
        ('video/quicktime', '.mov (video)'),
        ('application/pdf', '.pdf (document)'),
        ('image/jpeg', '.jpg, .jpeg, .jpe (image)')
    )
    MEDIUM_CHOICES = (
        ('Audio', 'Audio'),
        ('Video', 'Video'),
        ('Document', 'Document'),
        ('Image', 'Image'),
        ('Executable', 'Executable'),
    )
    EXPRESSION_CHOICES = (
        ('Sample', 'Sample'),
        ('Full', 'Full'),
        ('Nonstop', 'Non-stop'),
    )
    ALGO_CHOICES = (
        ('MD5', 'MD5'),
        ('SHA-1', 'SHA-1'),
    )
    title = models.CharField(max_length=255, blank=True, help_text='Title is generally only useful with multiple enclosures.')
    file = models.FileField(upload_to='podcasts/episodes/files/', help_text='Either upload or use the "Player" text box below. If uploading, file must be less than or equal to 30 MB for a Google video sitemap.', blank=True, null=True)
    mime = models.CharField('Format', max_length=255, choices=MIME_CHOICES, default='video/mp4', blank=True)
    medium = models.CharField(max_length=255, blank=True, choices=MEDIUM_CHOICES)
    expression = models.CharField(max_length=25, blank=True, choices=EXPRESSION_CHOICES, default='Full')
    frame = models.CharField('Frame rate', max_length=5, blank=True, help_text='Measured in frames per second (fps), often 29.97.')
    bitrate = models.CharField('Bit rate', max_length=5, blank=True, help_text='Measured in kilobits per second (kbps), often 128 or 192.')
    sample = models.CharField('Sample rate', max_length=5, blank=True, help_text='Measured in kilohertz (kHz), often 44.1.')
    channel = models.CharField(max_length=5, blank=True, help_text='Number of channels; 2 for stereo, 1 for mono.')
    algo = models.CharField('Hash algorithm', max_length=50, blank=True, choices=ALGO_CHOICES)
    hash = models.CharField(max_length=255, blank=True, help_text='MD-5 or SHA-1 file hash.')
    player = models.URLField(help_text='URL of the player console that plays the media. Could be your own .swf, but most likely a YouTube URL, such as <a href="http://www.youtube.com/v/UZCfK8pVztw">http://www.youtube.com/v/UZCfK8pVztw</a> (not the permalink, which looks like <a href="http://www.youtube.com/watch?v=UZCfK8pVztw">http://www.youtube.com/watch?v=UZCfK8pVztw</a>).', blank=True)
    embed = models.BooleanField(help_text='Check to allow Google to embed your external player in search results on <a href="http://video.google.com">Google Video</a>.', blank=True)
    width = models.PositiveIntegerField(blank=True, null=True, help_text='Width of the browser window in <br />which the URL should be opened. <br />YouTube\'s default is 425.')
    height = models.PositiveIntegerField(blank=True, null=True, help_text='Height of the browser window in <br />which the URL should be opened. <br />YouTube\'s default is 344.')
    episode = models.ForeignKey(Episode, help_text='Include any number of media files; for example, perhaps include an iPhone-optimized, AppleTV-optimized and Flash Video set of video files. Note that the iTunes feed only accepts the first file. More uploading is available after clicking "Save and continue editing."')

    class Meta:
        ordering = ['mime', 'file']

    def __unicode__(self):
        return u'%s' % (self.file)
