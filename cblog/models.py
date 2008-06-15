from django.db import models
from utils import slugifyUniquely
from tagging.fields import TagField
import markup_handler

class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
    			    unique=True, 
    			    prepopulate_from=('title',),
    			    blank=False)
    date = models.DateTimeField(auto_now_add=True)
    post = models.TextField()
    markup = models.CharField(max_length=255, default="html")
    post_generated_html = models.TextField(editable=False)
    post_generated_preview = models.TextField(editable=False)

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
        #till now we only support html Markup
        self.post_generated_html    = markup_handler.markup_to_html(self.post, 
                                                                    self.markup)
        self.post_generated_preview = markup_handler.markup_to_html(self.post, 
                                                                    self.markup)
        
        super(self.__class__, self).save()
            
        
    
    class Admin: 
        list_display = ('title', 'date')
