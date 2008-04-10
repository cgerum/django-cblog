from django.db import models
from utils import slugifyUniquely

try:
    from tagging.fields import TagField

except ImportError:
    class TagField(models.CharField):
        def __init__(self, **kwargs):
            default_kwargs = {'max_length': 255, 'blank': True}
            default_kwargs.update(kwargs)
            super(TagField, self).__init__(**default_kwargs)
        def get_internal_type(self):
            return 'CharField'

    #tagfield_help_text = _('Django-tagging was not found, tags will be treated as plain text.')
    
class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
    			    unique=True, 
    			    prepopulate_from=('title',),
    			    blank=False)
    date = models.DateTimeField(auto_now_add=True)
    post = models.TextField()
    
    tags = TagField(blank=True)

    def get_absolute_url(self):
        return ('blog_detail', [self.slug])

    get_absolute_url = models.permalink(get_absolute_url)
    
    def save(self):
        #Automatically slugifies from User title
        if not self.id:
            #Autopopulate fields
            if self.slug:
                value = self.slug
            else:
                value = self.title
            self.slug = slugifyUniquely(value, self.__class__)
        super(self.__class__, self).save()
            
        
    
    class Admin: 
        list_display = ('title', 'date')


#tagging.register(Blogpost)
