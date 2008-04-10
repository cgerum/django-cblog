from django import newforms as forms
from cblog.models import Blogpost 
from django.newforms.util import smart_unicode
from django.newforms.widgets import flatatt
from django.utils.safestring import mark_safe

#class PostEditField(forms.widgets.Textarea):
#    def render(self, name, value, attrs=None):
#        value = smart_unicode(value)
#        attrs = self.build_attrs(attrs, name=name)
#        
#        return mark_safe(u'<textarea %s>%s</textarea>' % (flatatt(attrs), value))

class EditPostForm(forms.ModelForm):
    #post = forms.fields.CharField(widget=PostEditField())
    class Meta:
        model = Blogpost
        exclude = ('slug',)
    
