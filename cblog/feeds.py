from django.conf import settings
from django.contrib.syndication.feeds import Feed
from django.contrib.sites.models import Site
from django.db.models import permalink
from django.utils.feedgenerator import Atom1Feed
from cblog.models import Blogpost
#from cblog.settings import FEED_LENGTH
FEED_LENGTH=10

class RssSiteNewsFeed(Feed):
    
    site = Site.objects.get(id=settings.SITE_ID)
    title = site.name
    description = 'Recent Blog Entries'
    
    link = permalink(lambda self: ('blog_index', []))
    
    description_template = 'feed/description.html'

    def items(self):
        return Blogpost.objects.all()[:FEED_LENGTH]
    
    def item_link(self, obj):
        return obj.get_absolute_url()
    
    
class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description 
