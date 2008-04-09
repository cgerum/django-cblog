from django.db import models
from tagging.fields import TagField
from utils import slugifyUniquely

import tagging

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
