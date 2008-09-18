from django.db import models
from django.contrib.auth.models import User
from podcast.managers import EpisodeManager


class Organization(models.Model):
    """Organization model."""
    name = models.CharField(max_length=255, help_text='Name of the organization or company producing the podcast.')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % (self.name)
    

class Category(models.Model):
    """Category model."""
    NAME_CHOICES = (
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
        ('Comdey', 'Comedy'),
        ('Education', (
                ('Education Technology', 'Education Technology'),
                ('Higher Education', 'Higher Education'),
                ('K-12', 'K-12'),
                ('Language Courses', 'Language Courses'),
                ('Training', 'Training'),
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
        ('Kids & Family', 'Kids & Family'),
        ('Music', 'Music'),
        ('News & Politics', 'News & Politics'),
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
        ('TV & Film', 'TV & Film'),
    )
    name = models.CharField(max_length=26, choices=NAME_CHOICES)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return u'%s' % (self.name)


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
    organization = models.ForeignKey(Organization, default=1)
    author = models.ManyToManyField(User, help_text='Remember to save the user\'s name and e-mail address in the User application.')
    webmaster = models.ForeignKey(User, blank=True, help_text='Remember to save the user\'s name and e-mail address in the User application.')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, help_text='Auto-generated based on title.')
    subtitle = models.CharField(max_length=255, help_text='Looks best if only a few words long like a tagline.')
    language = models.CharField(max_length=5, default='en-us', help_text='Default is American English. See <a href="http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">ISO 639-1</a> and <a href="http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements">ISO 3166-1</a> for more language codes.')
    description = models.TextField(help_text='Describe subject matter, media format, episode schedule and other relevant information while incorporating keywords.')
    summary = models.TextField(help_text='iTunes-specific description, which allows 4,000 characters. Description will be used if summary is blank.', blank=True)
    image = models.ImageField(upload_to='podcasts/shows/img/', help_text='An attractive, original square JPEG (.jpg) or PNG (.png) image of 600x600 pixels; will be scaled down to 50x50 pixels at smallest.')
    player = models.FileField(upload_to='podcasts/shows/players/', help_text='An optional Adobe Shockwave Flash (.swf) video player that loads external videos, for inclusion in a Google video sitemap.', blank=True)
    keywords = models.CharField(max_length=255, help_text='A comma-separated list of words for iTunes searches, up to 12; perhaps include misspellings of title.')
    explicit = models.CharField(max_length=255, default='no', choices=EXPLICIT_CHOICES, help_text='"Clean" will put the clean iTunes graphic by it.')
    block = models.BooleanField(default=False, help_text='Check to block this show from iTunes; show will remain blocked until unchecked.')
    link = models.URLField(help_text='URL of the main website or the podcast section of the main website.')
    ttl = models.PositiveIntegerField(help_text='"Time to Live," the number of minutes a channel can be cached before refreshing.')
    feedburner = models.URLField('FeedBurner URL', help_text='Fill this out after saving this show and at least one podcast. URL should look like "http://feeds.feedburner.com/TitleOfShow". See <a href="http://code.google.com/p/django-podcast/">documentation</a> for more.', blank=True)
    itunes = models.URLField('iTunes Store URL', help_text='Fill this out after saving this show and at least one podcast. URL should look like "http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewPodcast?id=000000000". See <a href="http://code.google.com/p/django-podcast/">documentation</a> for more.', blank=True)
    redirect = models.URLField(help_text='If changing URL of the new podcast feed. Must continue old feed for at least two weeks and write a 301 redirect for old feed.', blank=True)
    copyright = models.CharField(max_length=255, default='All rights reserved', choices=COPYRIGHT_CHOICES, help_text='See <a href="http://creativecommons.org/about/license/">Creative Commons licenses</a> for more information.')
    copyright_url = models.URLField(blank=True, help_text='A URL pointing to additional copyright information; consider a <a href="http://creativecommons.org/licenses/">Creative Commons license URL</a>.')
    category = models.ManyToManyField(Category, help_text='Selecting multiple categories makes the podcast more likely to be found by users.')

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return u'%s' % (self.title)

    def get_absolute_url(self):
        return '%s/' % (self.slug)


class Episode(models.Model):
    """Episode model."""
    SECONDS_CHOICES = tuple(('%02d' % x, str(x)) for x in range(60))
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
        ('Sample', 'Sample: A sample version of the object'),
        ('Full', 'Full: A full version of the object'),
        ('Nonstop', 'Non-stop: A continuous stream of the object'),
    )
    EXPLICIT_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Clean', 'Clean'),
    )
    SCHEME_CHOICE = (
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
        ('Assistant Camera', 'Assistant Camera')
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
        ('Focus Puller', 'Focus Puller')
        ('Foley Artist', 'Foley Artist')
        ('Foley Editor', 'Foley Editor'),
        ('Foley Mixer', 'Foley Mixer'),
        ('Graphic Assistant', 'Graphic Assistant')
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
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
        (3, _('Private')),
    )
    TYPE_CHOICES = (
        ('Plain', 'Plain'),
        ('HTML', 'HTML'),
    )
    show = models.ForeignKey(Show)
    author = models.ForeignKey(User, help_text='Remember to save the user\'s name and e-mail address in the User application.')
    title = models.CharField(max_length=255, help_text='Make it specific but avoid explicit language. Limit to 100 characters for inclusion in a Google video sitemap.')
    title_type = models.CharField('Title type', max_length=255, blank=True, choices=TYPE_CHOICES)
    slug = models.SlugField(unique=True, help_text='Auto-generated from title.')
    subtitle = models.CharField(max_length=255, help_text='Looks best if only a few words long like a tagline.')
    description = models.TextField(help_text='Avoid explicit language; allows 2,048 characters for inclusion in a Google video sitemap.')
    description_type = models.CharField('Description type', max_length=255, blank=True, choices=TYPE_CHOICES)
    summary = models.TextField(help_text='iTunes-specific description; allows 4,000 characters. Description will be used if summary is blank.', blank=True)
    minutes = models.PositiveIntegerField()
    seconds = models.CharField(max_length=2, choices=SECONDS_CHOICES)
    expression = models.CharField(blank=True, choices=EXPRESSION_CHOICES, help_text='Sample, full or streaming version of the file.')
    frame = models.CharField('Frame rate', max_length=5, blank=True, help_text='Measured in frames per second (fps), often 29.97.')
    bitrate = models.CharField('Bit rate', max_length=5, blank=True, help_text='Measured in kilobits per second (kbps), often 128 or 192.')
    sample = models.CharField('Sample rate', max_length=5, blank=True, help_text='Measured in kilohertz (kHz), often 44.1.')
    channel = models.CharField(blank=True, help_text='Number of channels; 2 for stereo, 1 for mono.')
    file = models.FileField(upload_to='podcasts/episodes/files/', help_text='Must be less than or equal to 30 MB for inclusion in a Google video sitemap.')
    image = models.ImageField(upload_to='podcasts/episodes/img/', help_text='A screenshot from the video for inclusion in a Google video sitemap. For podcast artwork to display in iTunes, image must be saved to file\'s metadata before uploading!', blank=True)
    mime = models.CharField('Format', max_length=255, choices=MIME_CHOICES, default='video/mp4')
    medium = models.CharField(max_length=255, blank=True, choices=MEDIUM_CHOICES)
    captions = models.FileField(upload_to='podcasts/episodes/captions/', help_text='For video podcasts; file type agnostic, but good choices include <a href="http://en.wikipedia.org/wiki/SubViewer">SubViewer</a>, <a href="http://en.wikipedia.org/wiki/SubRip">SubRip</a> or <a href="http://www.w3.org/TR/ttaf1-dfxp/">TimedText</a>.', blank=True)
    text = models.TextField(blank=True, help_text='Media RSS text transcript. Please see the <a href="http://search.yahoo.com/mrss/">Media RSS 2.0</a> spec for syntax.')
    category = models.CharField(max_length=255, blank=True, help_text='An optional, author-defined and episode-specific category. Probably not needed.')
    keywords = models.CharField(max_length=255, help_text='A comma-separated list of words for searches, up to 12; perhaps include misspellings.')
    explicit = models.CharField(max_length=255, choices=EXPLICIT_CHOICES, help_text='"Clean" will put the clean iTunes graphic by it.', default='no')
    scheme = models.CharField(max_length=255, blank=True, choices=SCHEME_CHOICES)
    rating = models.CharField(max_length=255, blank=True, choices=RATING_CHOICES, help_text='If used, Rating sub-selection must match Scheme selection.')
    role = models.CharField(max_length=255, blank=True, choices=ROLE_CHOICES, help_text='Role codes provided by the <a href="http://www.ebu.ch/en/technical/metadata/specifications/role_codes.php">European Broadcasting Union</a>.')
    block = models.BooleanField(help_text='Check to block this episode from iTunes because its content might cause the entire show to be removed from iTunes.', default=False)
    ALGO_CHOICES = (
        ('MD5', 'MD5'),
        ('SHA-1', 'SHA-1'),
    )
    algo = models.CharField(max_length=50, blank=True, choices=ALGO_CHOICES)
    hash = models.CharField(max_length=255, blank=True, help_text='MD-5 or SHA-1 hash of file.')
    embed = models.BooleanField(help_text='Check to allow Google to embed video in search results on <a href="http://video.google.com">Google Video</a>. Note: Will only work if .swf player is uploaded in respective Show.')
    RELATIONSHIP_CHOICES = (
        ('Allow', 'Allow'),
        ('Deny', 'Deny'),
    )
    relationship = models.CharField(max_length=50, blank=True, choices=RELATIONSHIP_CHOICES)
    SCOPE_CHOICES = (
        ('Country', 'Country'),
        ('URI', 'URI'),
    )
    scope = models.CharField(max_length=50, blank=True, choices=SCOPE_CHOICES)
    restriction = models.CharField(max_length=255, blank=True, help_text='A space-separated list of either <a href="http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements">ISO 3166-1-coded countries</a>, or URIs.')
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    date = models.DateTimeField(auto_now_add=True)
    objects = EpisodeManager()

    class Meta:
        ordering = ['-date', 'author', 'title']

    def __unicode__(self):
        return u'%s' % (self.title)

    def get_absolute_url(self):
        return '%s/' % (self.slug)

    def seconds_total(self):
        try:
            return (((float(self.minutes)) * 60) + (float(self.seconds)))
        except:
            return 0