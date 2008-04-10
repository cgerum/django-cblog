from django.conf.urls.defaults import *
from cblog.models import Blogpost
from cblog.feeds import RssSiteNewsFeed, AtomSiteNewsFeed
import tagging.views

entry_list_dict = { 
    'queryset' : Blogpost.objects.all().order_by('-date'),
    'template_name' : 'blog/blog_index.html',
    'allow_empty' : True,
    'paginate_by' : 10,
    }

entry_dict = {
    'queryset': Blogpost.objects.all().order_by('-date'),
    'template_name': 'blog/blog_detail.html',
    'slug_field': 'slug',
    'template_object_name': 'post',
    }

urlpatterns = patterns(
    'django.views.generic.list_detail',
    #(r'^$', 'cblog.views.index'),
    #(r'^posts/(?P<permalink>[\w-]+)$', 'cblog.views.detail'),
    #(r'^tags/(?P<tag>.+)$', 'cblog.views.tags'),
    url(r'^$', 'object_list', entry_list_dict, name='blog_index'),
    url(r'^entry/(?P<slug>[\w-]+)/$', 'object_detail', entry_dict, name='blog_detail')
)


#Feeds

feed_dict = {
    'feed_dict': {
        'rss': RssSiteNewsFeed,
        'atom': AtomSiteNewsFeed,
    }
}


urlpatterns = urlpatterns + patterns('',
    url(r'^(?P<url>[a-z]+).xml$', 
    	       'django.contrib.syndication.views.feed',
               feed_dict, name='blog_feed'),
) 


#Tags

tag_list_dict =  {
    'queryset_or_model' : Blogpost.objects.all().order_by('-date'),
    #'model' : Blogpost, 
    'paginate_by' : 10, 
    'allow_empty' : True,
    'template_name' : 'blog/blog_index.html',
    }

urlpatterns = urlpatterns + patterns('',
    url(r'^tag/(?P<tag>[^/]+)/$',
        'tagging.views.tagged_object_list',
        tag_list_dict,
        name='blogpost_tag'),
)


#Edit

urlpatterns = urlpatterns + patterns('',
                                     url(r'^entry/(?P<slug>[\w-]+)/edit/$', 
                                         'cblog.views.edit_article', 
                                         name='edit_post'),
                                     url(r'^add_entry/$', 
                                         'cblog.views.edit_article',
                                         name='new_post'),
)
