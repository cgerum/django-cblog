from django import newforms as forms
from cblog.models import Blogpost

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        exclude = ('slug',)
    
