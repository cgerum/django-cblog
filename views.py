from django.shortcuts import render_to_response
from cblog.models import Blogpost
from tagging.models import Tag, TaggedItem
from cblog.forms import EditPostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def edit_article(request, slug=""):
    if slug:
        blogpost = Blogpost.objects.filter(slug=slug)[0]
    else:
        blogpost = None

    if request.POST:
        form = EditPostForm(data=request.POST, instance=blogpost)
        model = form.save(commit=False);
        if request.POST.has_key('ajax'):
            data = render_to_response('blog/blog_post.html',
                                      {'post' : model})
            return HttpResponse(data, mimetype="text/html")
        model.save()
        return HttpResponseRedirect(reverse('blog_detail', kwargs={'slug' : slug}))
    
    form  = EditPostForm(instance=blogpost)
    return render_to_response ('blog/blog_edit.html', {'form' : form})
